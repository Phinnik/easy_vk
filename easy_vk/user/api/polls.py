from typing import List, Union, Optional
from easy_vk.types import objects, responses
from .base import BaseCategory


class Polls(BaseCategory):
    def __init__(self, session, access_token: str, v: str, delay: float, auto_retry: bool, max_retries: int, timeout: float):
        super().__init__(session, access_token, v, delay, auto_retry, max_retries, timeout)

    def add_vote(self, owner_id: int = None, poll_id: int = None, answer_ids: List[int] = None, is_board: bool = None) -> responses.PollsAddVote:
        """
        Adds the current user's vote to the selected answer in the poll.
        
        :param owner_id: ID of the user or community that owns the poll. Use a negative value to designate a community ID.
        :param poll_id: Poll ID.
        :param answer_ids: 
        :param is_board: 
        """
    
        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        method_name = 'polls.addVote'
        param_aliases = []
        response_type = responses.PollsAddVote
        return self._call(method_name, method_parameters, param_aliases, response_type)

    def create(self, question: str = None, is_anonymous: bool = None, is_multiple: bool = None, end_date: int = None, owner_id: int = None, add_answers: str = None, photo_id: int = None, background_id: str = None, disable_unvote: bool = None) -> responses.PollsCreate:
        """
        Creates polls that can be attached to the users' or communities' posts.
        
        :param question: question text
        :param is_anonymous: '1' – anonymous poll, participants list is hidden,, '0' – public poll, participants list is available,, Default value is '0'.
        :param is_multiple: 
        :param end_date: 
        :param owner_id: If a poll will be added to a communty it is required to send a negative group identifier. Current user by default.
        :param add_answers: available answers list, for example: " ["yes","no","maybe"]", There can be from 1 to 10 answers.
        :param photo_id: 
        :param background_id: 
        :param disable_unvote: 
        """
    
        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        method_name = 'polls.create'
        param_aliases = []
        response_type = responses.PollsCreate
        return self._call(method_name, method_parameters, param_aliases, response_type)

    def delete_vote(self, owner_id: int = None, poll_id: int = None, answer_id: int = None, is_board: bool = None) -> responses.PollsDeleteVote:
        """
        Deletes the current user's vote from the selected answer in the poll.
        
        :param owner_id: ID of the user or community that owns the poll. Use a negative value to designate a community ID.
        :param poll_id: Poll ID.
        :param answer_id: Answer ID.
        :param is_board: 
        """
    
        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        method_name = 'polls.deleteVote'
        param_aliases = []
        response_type = responses.PollsDeleteVote
        return self._call(method_name, method_parameters, param_aliases, response_type)

    def edit(self, owner_id: int = None, poll_id: int = None, question: str = None, add_answers: str = None, edit_answers: str = None, delete_answers: str = None, end_date: int = None, photo_id: int = None, background_id: str = None) -> responses.BaseOk:
        """
        Edits created polls
        
        :param owner_id: poll owner id
        :param poll_id: edited poll's id
        :param question: new question text
        :param add_answers: answers list, for example: , "["yes","no","maybe"]"
        :param edit_answers: object containing answers that need to be edited,, key – answer id, value – new answer text. Example: {"382967099":"option1", "382967103":"option2"}"
        :param delete_answers: list of answer ids to be deleted. For example: "[382967099, 382967103]"
        :param end_date: 
        :param photo_id: 
        :param background_id: 
        """
    
        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        method_name = 'polls.edit'
        param_aliases = []
        response_type = responses.BaseOk
        return self._call(method_name, method_parameters, param_aliases, response_type)

    def get_by_id(self, owner_id: int = None, is_board: bool = None, poll_id: int = None, extended: bool = None, friends_count: int = None, fields: List[str] = None, name_case: str = None) -> responses.PollsGetById:
        """
        Returns detailed information about a poll by its ID.
        
        :param owner_id: ID of the user or community that owns the poll. Use a negative value to designate a community ID.
        :param is_board: '1' – poll is in a board, '0' – poll is on a wall. '0' by default.
        :param poll_id: Poll ID.
        :param extended: 
        :param friends_count: 
        :param fields: 
        :param name_case: 
        """
    
        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        method_name = 'polls.getById'
        param_aliases = []
        response_type = responses.PollsGetById
        return self._call(method_name, method_parameters, param_aliases, response_type)

    def get_voters(self, owner_id: int = None, poll_id: int = None, answer_ids: List[int] = None, is_board: bool = None, friends_only: bool = None, offset: int = None, count: int = None, fields: List[Union[objects.UsersFields, str]] = None, name_case: str = None) -> responses.PollsGetVoters:
        """
        Returns a list of IDs of users who selected specific answers in the poll.
        
        :param owner_id: ID of the user or community that owns the poll. Use a negative value to designate a community ID.
        :param poll_id: Poll ID.
        :param answer_ids: Answer IDs.
        :param is_board: 
        :param friends_only: '1' — to return only current user's friends, '0' — to return all users (default),
        :param offset: Offset needed to return a specific subset of voters. '0' — (default)
        :param count: Number of user IDs to return (if the 'friends_only' parameter is not set, maximum '1000', otherwise '10'). '100' — (default)
        :param fields: Profile fields to return. Sample values: 'nickname', 'screen_name', 'sex', 'bdate (birthdate)', 'city', 'country', 'timezone', 'photo', 'photo_medium', 'photo_big', 'has_mobile', 'rate', 'contacts', 'education', 'online', 'counters'.
        :param name_case: Case for declension of user name and surname: , 'nom' — nominative (default) , 'gen' — genitive , 'dat' — dative , 'acc' — accusative , 'ins' — instrumental , 'abl' — prepositional
        """
    
        method_parameters = {k: v for k, v in locals().items() if k not in {'self', 'raw_response'}}
        method_name = 'polls.getVoters'
        param_aliases = []
        response_type = responses.PollsGetVoters
        return self._call(method_name, method_parameters, param_aliases, response_type)

