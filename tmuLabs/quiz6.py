import unittest


class Partygoer():

    def __init__(self, name, costume, location="home", bedtime=2):
        self.name = name
        self.costume = costume
        self.location = location
        self.bedtime = bedtime

    def change_costume(self, new_costume):
        self.costume = new_costume

    def go_home(self):
        self.location = 'home'

    def go_to_party(self, halloween_party_to_go_to):
        if self.location == 'home':
            self.location = halloween_party_to_go_to
            return True
        return False


class HalloweenParty():
    def __init__(self, partyname, partygoers, current_time):

        self.partyname = partyname
        self.partygoers = partygoers
        self.current_time = current_time

    def remove_from_party(self, partygoer):

        if partygoer in self.partygoers:
            partygoer.go_home()
            self.partygoers.remove(partygoer)

    def add_to_party(self, partygoer):
        if partygoer not in self.partygoers:
            if partygoer.go_to_party(self):
                self.partygoers.append(partygoer)

    def party_police_bedtime_check(self):  # Method 6 (required)
        '''
        To make sure that people attend their morning labs, you've hired party police to check every partygoer at the party, and if the current time is greater
        than their bedtime, you must send them home.
        Input Arguments:
            None
        Return:
            None
        Behaviour:
            For all Partygoer instances in partygoers
                If the curent party's time is past their bedtime (you can assume parties go until midnight (0.00) at the earliest, and end at 23.59 at the latest, and that nobodies bedtime is before midnight)
                    Send them home via their go_home method
                    Then remove them from the partygoers list
                Otherwise
                    Do nothing - party on!!! (woot woot)
        '''
        for i in self.partygoers:
            if self.current_time > i.bedtime:
                i.location = 'home'
                self.partygoers.remove(i)

    def check_if_party_lit(self):  # Method 7 (bonus)
        '''
        According to my sister, for a party to be "lit" there must be at least 4 people there, it must be past midnight (0.00) and before 8 am (8.00), and the party must have Longevity
        Longevity is defined as: in 1 hour from the current time, at least 50% of the partygoers must still be there
        You can assume that partygoers will not leave a party unless it is past their bedtime for longevity checks
        Input Arguments:
            None
        Return:
            True if party is lit
            False otherwise
        Behaviour:
            Check if the party is lit.
            First ensure there are at least 4 people there (partygoers)
            Then ensure that it is currently past midnight and before 8 am (current_time)
            Then, for all current partygoers, ensure that for at least half of current partygoers, in 1 hour it is not past their bedtime
            If any of the above criteria fails the party is not lit. Otherwise it is.
        '''
        if len(self.partygoers) < 4:
            return False
        elif 0 >= self.current_time >= 8:
            return False
        counter = 0
        for i in self.partygoers:
            if abs(self.current_time - i.bedtime) <= 1:
                counter += 1
        if counter >= len(self.partygoers) // 2:
            return False
        return True

    def total_teletubby_takeover(self):  # Method 8 (bonus)
        '''
        I'd like to believe that Teletubbies are popular at parties. My mom always said, "be the change you want to see in the world".
        Input Arguments:
            None
        Return:
            None
        Behaviour:
            For all Partygoer instances in partygoers,
                Set their costume to some Teletubby ["Tinky Winky", "Laa-Laa", "Dipsy", "Po"]. Trends are contagious!
        '''
        ls = ["Tinky Winky", "Laa-Laa", "Dipsy", "Po"]
        counter = 0
        for i in self.partygoers:
            i.change_costume(ls[counter % 4])
            counter += 1


class HalloweenPartyTestCases(unittest.TestCase):
    def test_1_change_costume(self):  # YOU DO THIS (required)
        tp = Partygoer("Chris", "Batman")
        tp.change_costume('Teletubby')
        # How can you test if a costume change works?
        self.assertEqual(tp.costume, "Teletubby")

    def test_2_partygoer_initialization(self):
        tp = Partygoer("Chris", "Teletubby")
        self.assertEqual(tp.name, "Chris")
        self.assertEqual(tp.costume, "Teletubby")
        self.assertEqual(tp.location, "home")  # Recall default home
        self.assertEqual(tp.bedtime, 2)  # Recall default bedtime

    def test_3_partygoer_nondefault_initialization(self):
        tp = Partygoer("Chris", "Teletubby", bedtime=3)
        self.assertEqual(tp.name, "Chris")
        self.assertEqual(tp.costume, "Teletubby")
        self.assertEqual(tp.location, "home")  # Recall default home
        self.assertEqual(tp.bedtime, 3)  # Should override default bedtime

    def test_4_partygoer_go_home_already_home(self):
        tp = Partygoer("Chris", "Teletubby")
        tp.go_home()
        self.assertEqual(tp.location, "home")

    def test_5_partygoer_go_home_at_party(self):
        party = HalloweenParty("Chris' Awesome Party", [], 0.00)
        tp = Partygoer("Chris", "Teletubby")
        party.partygoers = [tp]  # Manual set
        tp.location = party  # Manual set
        tp.go_home()
        self.assertEqual(tp.location, "home")

    def test_6_partygoer_go_party_from_home(self):
        party = HalloweenParty("Chris' Awesome Party", [], 0.00)
        tp = Partygoer("Chris", "Teletubby")
        tp.location = "home"  # Manual set
        return_val = tp.go_to_party(party)
        self.assertTrue(return_val)
        self.assertEqual(tp.location, party)

    def test_7_partygoer_go_party_from_party(self):
        party1 = HalloweenParty("Chris' Awesome Party", [], 0.00)
        party2 = HalloweenParty("Saghar's Fantastic Party", [], 1.30)
        tp = Partygoer("Chris", "Teletubby")
        tp.location = party1  # Manual set
        return_val = tp.go_to_party(party2)
        self.assertFalse(return_val)
        self.assertEqual(tp.location, party1)

    def test_8_halloweenparty_initialization(self):
        tp = Partygoer("Chris", "Teletubby")
        tp2 = Partygoer("Daniel", "Terminator")
        party = HalloweenParty("Chris' Awesome Party", [tp, tp2], 0.00)
        self.assertEqual(party.partyname, "Chris' Awesome Party")
        self.assertEqual(party.partygoers, [tp, tp2])
        self.assertEqual(party.current_time, 0.00)

    def test_9_remove_from_party_present(self):
        tp = Partygoer("Chris", "Teletubby")
        tp2 = Partygoer("Daniel", "Terminator")
        party = HalloweenParty("Chris' Awesome Party", [tp, tp2], 0.00)
        tp.location = party  # Manual set
        tp2.location = party  # Manual set
        party.remove_from_party(tp)
        self.assertEqual(tp.location, "home")  # Check sent home
        self.assertEqual(party.partygoers, [tp2])  # Check removed from party

    def test_10_remove_from_party_not_present(self):
        party1 = HalloweenParty("Chris' Awesome Party", [], 0.00)
        tp = Partygoer("Chris", "Teletubby")
        party2 = HalloweenParty("Saghar's Fantastic Party", [tp], 1.30)
        tp.location = party2  # Manual set
        party1.remove_from_party(tp)
        # Check not removed from other party
        self.assertEqual(tp.location, party2)
        self.assertEqual(party1.partygoers, [])

    def test_11_add_to_party_present(self):
        tp = Partygoer("Chris", "Teletubby")
        tp2 = Partygoer("Daniel", "Terminator")
        party = HalloweenParty("Chris' Awesome Party", [tp, tp2], 0.00)
        tp.location = party  # Manual set
        tp2.location = party  # Manual set
        party.add_to_party(tp2)
        self.assertEqual(tp2.location, party)
        self.assertEqual(party.partygoers, [tp, tp2])

    def test_12_add_to_party_not_present_at_home(self):
        tp = Partygoer("Chris", "Teletubby")
        tp2 = Partygoer("Daniel", "Terminator")
        tp2.location = "home"  # Manual set
        party = HalloweenParty("Chris' Awesome Party", [tp], 0.00)
        tp.location = party  # Manual set
        party.add_to_party(tp2)
        self.assertEqual(tp2.location, party)
        self.assertEqual(party.partygoers, [tp, tp2])

    def test_13_add_to_party_not_present_other_party(self):
        party1 = HalloweenParty("Chris' Awesome Party", [], 0.00)
        party2 = HalloweenParty("Saghar's Fantastic Party", [], 1.30)
        tp = Partygoer("Chris", "Teletubby")
        tp2 = Partygoer("Daniel", "Terminator")
        party1.partygoers = [tp]  # Manual set
        party2.partygoers = [tp2]  # Manual set
        tp.location = party1  # Manual set
        tp2.location = party2  # Manual set
        party1.add_to_party(tp2)
        self.assertEqual(tp2.location, party2)
        self.assertEqual(party1.partygoers, [tp])

    # I'm only adding one test here but in a full suite there would be more...
    def test_14_party_police_bedtime_check(self):
        party1 = HalloweenParty("Chris' Awesome Party", [], 2.00)
        tp = Partygoer("Chris", "Teletubby")
        tp2 = Partygoer("Daniel", "Terminator")
        tp3 = Partygoer("Saghar", "Superhero")
        tp.bedtime = 0.30  # All manual sets so as to not depend on correct constructor
        tp2.bedtime = 4.00
        tp3.bedtime = 2.30
        tp.location = party1
        tp2.location = party1
        tp3.location = party1
        party1.partygoers = [tp, tp2, tp3]
        party1.party_police_bedtime_check()
        self.assertEqual(tp.location, "home")
        self.assertEqual(tp2.location, party1)
        self.assertEqual(party1.partygoers, [tp2, tp3])

    def test_15_bonus_check_if_party_lit(self):
        party1 = HalloweenParty("Chris' Awesome Party", [], 2.00)
        tp = Partygoer("Chris", "Teletubby")
        tp2 = Partygoer("Daniel", "Terminator")
        tp3 = Partygoer("Saghar", "Superhero")
        tp4 = Partygoer("Alex", "Supervillain")
        tp.bedtime = 0.30  # All manual sets so as to not depend on correct constructor
        tp2.bedtime = 4.00
        tp3.bedtime = 3.30
        tp4.bedtime = 5.00
        tp.location = party1
        tp2.location = party1
        tp3.location = party1
        tp4.location = party1
        party1.partygoers = [tp, tp2, tp3, tp4]
        self.assertTrue(party1.check_if_party_lit())

    def test_16_bonus_check_if_party_not_lit(self):
        party1 = HalloweenParty("Chris' Awesome Party", [], 3.00)
        tp = Partygoer("Chris", "Teletubby")
        tp2 = Partygoer("Daniel", "Terminator")
        tp3 = Partygoer("Saghar", "Superhero")
        tp4 = Partygoer("Alex", "Supervillain")
        tp.bedtime = 0.30  # All manual sets so as to not depend on correct constructor
        tp2.bedtime = 3.25
        tp3.bedtime = 3.30
        tp4.bedtime = 5.00
        tp.location = party1
        tp2.location = party1
        tp3.location = party1
        tp4.location = party1
        party1.partygoers = [tp, tp2, tp3, tp4]
        self.assertFalse(party1.check_if_party_lit())

    def test_17_bonus_check_if_all_teletubbies(self):
        party1 = HalloweenParty("Chris' Awesome Party", [], 2.00)
        tp = Partygoer("Chris", "Teletubby")
        tp2 = Partygoer("Daniel", "Terminator")
        party1.partygoers = [tp, tp2]
        party1.total_teletubby_takeover()
        all_good_switch = True
        for partygoer in party1.partygoers:
            if partygoer.costume not in ["Tinky Winky", "Dipsy", "Laa-Laa", "Po"]:
                all_good_switch = False
        self.assertTrue(all_good_switch)


if __name__ == "__main__":
    unittest.main(exit=True)
