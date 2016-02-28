"""
Manual testing of user class

Run `python ./test_user.py` and results should print out
"""
from user import user


def test_user():
    u1 = user(userName="JaneTest")
    u2 = user(userName="JoeTest")

    print "Created new user u1"
    print "u1.userName: " + str(u1.userName)
    print "u1.numMessagesToKeep: " + str(u1.numMessagesToKeep)


if __name__ == "__main__":
    test_user()
