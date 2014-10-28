
class Tweeter(object):

    def __init__(self, user_name, team, ttype, org,
                real_name=None):
        """
        POJO representing a tweeter.

        :param user_name: The twitter handle of the user.
        :param team: The team associated with the user; could be generic NHL
        :param ttype: The type of account ie. NHL, team, beatwriter, player etc
        :param org: The organization associated ie. NHL, TSN, ESPN, Newspaper
        :param real_name: (Optional) The real name of the person behind the
            handle
        """
        self._user_name = user_name
        self._team = team
        self._type = ttype
        self._org = org
        self._real_name = real_name

    @property
    def user_name(self):
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        self._user_name = user_name

    @property
    def team(self):
        return self._team

    @team.setter
    def team(self, team):
        self._team = team

    @property
    def ttype(self):
        return self._type

    @ttype.setter
    def ttype(self, ttype):
        self._type = ttype

    @property
    def org(self):
        return self._org

    @org.setter
    def org(self, org):
        self._org = org

    @property
    def real_name(self):
        return self._real_name

    @real_name.setter
    def real_name(self, real_name):
        self._real_name = real_name

