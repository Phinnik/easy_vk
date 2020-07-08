from ._ApiMethod import ApiMethod
from typing import List


class Polls(ApiMethod):
    def __init__(self, session, access_token, v, requests_per_s):
        super().__init__(session, access_token, v, requests_per_s)

    def add_vote(self, poll_id: int, answer_ids: List[int], owner_id: int = None, is_board: bool = None):
        """
        Adds the current user's vote to the selected answer in the poll.
        
        :param poll_id: Poll ID.
        :param answer_ids: 
        :param owner_id: ID of the user or community that owns the poll. Use a negative value to designate a community ID.
        :param is_board: 
        """
    
        if answer_ids:
            answer_ids = [str(a) for a in answer_ids]
            answer_ids = ','.join(answer_ids)
        
        method_name = 'polls.addVote'
        return self._call(method_name, locals())

    def create(self, question: str = None, is_anonymous: bool = None, is_multiple: bool = None, end_date: int = None, owner_id: int = None, add_answers: str = None, photo_id: int = None, background_id: str = None):
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
        """
    
        method_name = 'polls.create'
        return self._call(method_name, locals())

    def delete_vote(self, poll_id: int, answer_id: int, owner_id: int = None, is_board: bool = None):
        """
        Deletes the current user's vote from the selected answer in the poll.
        
        :param poll_id: Poll ID.
        :param answer_id: Answer ID.
        :param owner_id: ID of the user or community that owns the poll. Use a negative value to designate a community ID.
        :param is_board: 
        """
    
        method_name = 'polls.deleteVote'
        return self._call(method_name, locals())

    def edit(self, poll_id: int, owner_id: int = None, question: str = None, add_answers: str = None, edit_answers: str = None, delete_answers: str = None, end_date: int = None, photo_id: int = None, background_id: str = None):
        """
        Edits created polls
        
        :param poll_id: edited poll's id
        :param owner_id: poll owner id
        :param question: new question text
        :param add_answers: answers list, for example: , "["yes","no","maybe"]"
        :param edit_answers: object containing answers that need to be edited,, key – answer id, value – new answer text. Example: {"382967099":"option1", "382967103":"option2"}"
        :param delete_answers: list of answer ids to be deleted. For example: "[382967099, 382967103]"
        :param end_date: 
        :param photo_id: 
        :param background_id: 
        """
    
        method_name = 'polls.edit'
        return self._call(method_name, locals())

    def get_by_id(self, poll_id: int, owner_id: int = None, is_board: bool = None, extended: bool = None, friends_count: int = None, fields: List[str] = None, name_case: str = None):
        """
        Returns detailed information about a poll by its ID.
        
        :param poll_id: Poll ID.
        :param owner_id: ID of the user or community that owns the poll. Use a negative value to designate a community ID.
        :param is_board: '1' – poll is in a board, '0' – poll is on a wall. '0' by default.
        :param extended: 
        :param friends_count: 
        :param fields: 
        :param name_case: 
        """
    
        if fields:
            fields = ','.join(fields)
        
        method_name = 'polls.getById'
        return self._call(method_name, locals())

    def get_voters(self, poll_id: int, answer_ids: List[int], owner_id: int = None, is_board: bool = None, friends_only: bool = None, offset: int = None, count: int = None, fields: List[str] = None, name_case: str = None):
        """
        Returns a list of IDs of users who selected specific answers in the poll.
        
        :param poll_id: Poll ID.
        :param answer_ids: Answer IDs.
        :param owner_id: ID of the user or community that owns the poll. Use a negative value to designate a community ID.
        :param is_board: 
        :param friends_only: '1' — to return only current user's friends, '0' — to return all users (default),
        :param offset: Offset needed to return a specific subset of voters. '0' — (default)
        :param count: Number of user IDs to return (if the 'friends_only' parameter is not set, maximum '1000', otherwise '10'). '100' — (default)
        :param fields: Profile fields to return. Sample values: 'nickname', 'screen_name', 'sex', 'bdate (birthdate)', 'city', 'country', 'timezone', 'photo', 'photo_medium', 'photo_big', 'has_mobile', 'rate', 'contacts', 'education', 'online', 'counters'.
        :param name_case: Case for declension of user name and surname: , 'nom' — nominative (default) , 'gen' — genitive , 'dat' — dative , 'acc' — accusative , 'ins' — instrumental , 'abl' — prepositional
        """
    
        if answer_ids:
            answer_ids = [str(a) for a in answer_ids]
            answer_ids = ','.join(answer_ids)
        if fields:
            fields = ','.join(fields)
        
        method_name = 'polls.getVoters'
        return self._call(method_name, locals())

