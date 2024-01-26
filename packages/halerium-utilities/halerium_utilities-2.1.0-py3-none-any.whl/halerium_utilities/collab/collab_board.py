import httpx
import logging
import os
from pathlib import Path
from typing import Any, Dict, Union
from urllib.parse import urljoin, quote

from halerium_utilities.board.board import Board
from halerium_utilities.board import schemas
from halerium_utilities.collab import schemas as collab_schemas
from halerium_utilities.logging.exceptions import (
    BoardConnectionError, DuplicateIdError, BoardUpdateError, IdNotFoundError)


class CollabBoard(Board):
    """
    Extension of the board class to communicate with the collaboration server.

    The class provides additional pull and push methods to keep the in-memory
    board in sync with the one of the collaboration server. The class is designed
    to be used on a runner but can be initialized elsewhere as well with the
    optional arguments in the init.
    """

    def __init__(self, path: Union[str, Path, os.PathLike],
                 url: str = None, headers: Dict[str, Any] = None,
                 pull_on_init=True,
                 check_if_path_exists=True):

        if url is None:
            tenant = os.getenv('HALERIUM_TENANT_KEY', '')
            workspace = os.getenv('HALERIUM_PROJECT_ID', '')
            runner_id = os.getenv('HALERIUM_ID', '')
            base_url = os.getenv('HALERIUM_BASE_URL', '')

            url = urljoin(base_url,
                          f"/api/tenants/{quote(tenant, safe='')}"
                          f"/projects/{quote(workspace, safe='')}"
                          f"/runners/{quote(runner_id, safe='')}"
                          "/collab")
        self.url = url

        if headers is None:
            headers = {'halerium-runner-token': os.getenv('HALERIUM_TOKEN', '')}
        self.headers = headers

        self.path = Path(path)
        if check_if_path_exists:
            if not self.path.exists():
                raise FileNotFoundError(f"{self.path} could not be found.")
            if not self.path.suffix == ".board":
                raise ValueError(".board file expected.")

        self._actions = []

        super().__init__(board=None)

        if pull_on_init:
            self.pull()

    def __eq__(self, other):
        if isinstance(other, CollabBoard):
            return (self._board == other._board and
                    self._actions == other._actions)
        return False

    def _get_file_url(self):
        file_url = urljoin(self.url,
                           quote(self.path.as_posix(), safe=''))
        return file_url

    def _reapply_actions(self):
        for action in self._actions:
            try:
                if action.type == "add_node":
                    super().add_card(action.payload.dict(exclude_none=True))
                elif action.type == "add_edge":
                    super().add_connection(action.payload.dict(exclude_none=True))
                elif action.type == "remove_node":
                    super().remove_card(action.payload.dict(exclude_none=True))
                elif action.type == "remove_edge":
                    super().remove_connection(action.payload.dict(exclude_none=True))
                elif action.type == "update_node":
                    super().update_card(action.payload.dict(exclude_none=True))
                elif action.type == "update_edge":
                    super().update_connection(action.payload.dict(exclude_none=True))
                elif action.type == "update_process_queue":
                    pass
                else:
                    raise TypeError(f"Unknown action type {action.type}.")
            except (BoardConnectionError, BoardUpdateError,
                    IdNotFoundError, DuplicateIdError) as exc:
                logging.warning(f"Action {action} could not be applied ({exc}).")

    def pull(self):
        with httpx.Client() as httpx_client:
            response = httpx_client.get(self._get_file_url(),
                                        headers=self.headers)
        response.raise_for_status()
        board_dict = response.json()["data"]
        self._board = schemas.Board.validate(board_dict)

    async def pull_async(self):
        async with httpx.AsyncClient() as httpx_client:
            response = await httpx_client.get(self._get_file_url(),
                                              headers=self.headers)
        response.raise_for_status()
        board_dict = response.json()["data"]
        self._board = schemas.Board.validate(board_dict)

    def _prepare_actions_data(self):
        data = collab_schemas.BoardActions.validate(
            {"actions": self._actions}).dict(exclude_none=True)
        return data

    def _flush_actions(self):
        self._actions = []

    def push(self):
        if len(self._actions) == 0:
            return None

        data = self._prepare_actions_data()
        with httpx.Client() as httpx_client:
            response = httpx_client.post(self._get_file_url(),
                                         headers=self.headers,
                                         json=data)
        response.raise_for_status()
        self._flush_actions()

    async def push_async(self):
        if len(self._actions) == 0:
            return None

        data = self._prepare_actions_data()
        async with httpx.AsyncClient() as httpx_client:
            response = await httpx_client.post(self._get_file_url(),
                                               headers=self.headers,
                                               json=data)
        response.raise_for_status()
        self._flush_actions()

    def add_card(self, card: Union[dict, schemas.Node]):
        if not isinstance(card, schemas.Node):
            card = schemas.Node.validate(card)
        action = collab_schemas.BoardAction.validate(
            {"type": "add_node",
             "payload": card}
        )
        super().add_card(card)
        self._actions.append(action)
    add_card.__doc__ = Board.add_card.__doc__

    def add_connection(self, connection: Union[dict, schemas.Edge]):
        if not isinstance(connection, schemas.Edge):
            connection = schemas.Edge.validate(connection)
        action = collab_schemas.BoardAction.validate(
            {"type": "add_edge",
             "payload": connection}
        )
        super().add_connection(connection)
        self._actions.append(action)
    add_connection.__doc__ = Board.add_connection.__doc__

    def remove_card(self, card: Union[Dict, schemas.Node]):
        if not isinstance(card, schemas.id_schema.NodeId):
            card = schemas.id_schema.NodeId.validate(card)
        card_id = card.id
        action = collab_schemas.BoardAction.validate(
            {"type": "remove_node",
             "payload": {"id": card_id}}
        )
        super().remove_card(card)
        self._actions.append(action)
    remove_card.__doc__ = Board.remove_card.__doc__

    def remove_connection(self, connection: Union[Dict, schemas.Edge]):
        if not isinstance(connection, schemas.id_schema.EdgeId):
            connection = schemas.id_schema.EdgeId.validate(connection)
        connection_id = connection.id
        action = collab_schemas.BoardAction.validate(
            {"type": "remove_edge",
             "payload": {"id": connection_id}}
        )
        super().remove_connection(connection)
        self._actions.append(action)
    remove_connection.__doc__ = Board.remove_connection.__doc__

    def update_card(self, card_update: Union[Dict, schemas.NodeUpdate]):
        if not isinstance(card_update, schemas.NodeUpdate):
            if "type" not in card_update:
                card_update["type"] = self.get_card_by_id(card_update["id"]).type
            card_update = schemas.NodeUpdate.validate(card_update)

        action = collab_schemas.BoardAction.validate(
            {"type": "update_node",
             "payload": card_update.dict(exclude_none=True)}
        )
        super().update_card(card_update)
        self._actions.append(action)
    update_card.__doc__ = Board.update_card.__doc__

    def update_connection(self, connection_update: Union[Dict, schemas.EdgeUpdate]):
        if not isinstance(connection_update, schemas.EdgeUpdate):
            if "type" not in connection_update:
                connection_update["type"] = self.get_connection_by_id(
                    connection_update["id"]).type
            connection_update = schemas.EdgeUpdate.validate(connection_update)

        action = collab_schemas.BoardAction.validate(
            {"type": "update_edge",
             "payload": connection_update.dict(exclude_none=True)}
        )
        super().update_connection(connection_update)
        self._actions.append(action)
    update_connection.__doc__ = Board.update_connection.__doc__

    def update_process_queue(
            self, process_queue_update: Union[Dict, collab_schemas.ProcessQueueUpdate]):
        """
        Update the processing queue for prompts.


        Parameters
        ----------
        process_queue_update Union[Dict, collab_schemas.ProcessQueueUpdate]):
            The patter is `{"id": node_id, "continue_prompt": bool, "end": bool}.
            The "continue_prompt" parameter governs whether to continue the prompt process.
            The "end" parameter governs whether to push to the end (true) or the beginning (false) of the queue.

        Returns
        -------
        """
        # if isinstance(process_queue_update, collab_schemas.ProcessQueueUpdate):
        #     process_queue_update = process_queue_update.dict(exclude_none=True)
        action = collab_schemas.BoardAction.validate(
            {"type": "update_process_queue",
             "payload": process_queue_update}
        )
        self._actions.append(action)
