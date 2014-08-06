import datetime
from django.utils import timezone
from django.test import TestCase
from django.core.urlresolvers import reverse
from adventure_time.models import World


class WorldMethodTests(TestCase):

    def test_was_created_recently_with_future_world(self):
        """ was_created_recently() should return False for worlds whose
        creation_date is in the future
        """
        future_world = World(creation_date=timezone.now() + datetime.timedelta(days=30))
        self.assertEqual(future_world.was_created_recently(), False)

    def test_was_created_recently_with_old_world(self):
        """ was_created_recently() should return False for worlds whose
        creation_date is older than 1 day
        """
        old_world = World(creation_date=timezone.now() - datetime.timedelta(days=30))
        self.assertEqual(old_world.was_created_recently(), False)

    def test_was_created_recently_with_recent_world(self):
        """ was_created_recently() should return True for worlds whose
        creation_date is within the last day
        """
        recent_world = World(creation_date=timezone.now() - datetime.timedelta(hours=1))
        self.assertEqual(recent_world.was_created_recently(), True)


def create_world(name, days):
    """ Creates a world with the given `name` created the given number of `days`
    offset to now (negative for worlds created in the past, positive for worlds
    that have yet to be created).
    """
    return World.objects.create(name=name, creation_date=timezone.now() + datetime.timedelta(days=days))


class WorldViewTests(TestCase):

    def test_index_view_with_no_worlds(self):
        """ If no world exist, an appropriate message should be displayed.
        """
        response = self.client.get(reverse('adventure_time:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No worlds are available.")
        self.assertQuerysetEqual(response.context['latest_world_list'], [])

    def test_index_view_with_a_past_world(self):
        """ Worlds with a creation_date in the past should be displayed on the
        index page.
        """
        create_world(name="Past world.", days=-30)
        response = self.client.get(reverse('adventure_time:index'))
        self.assertQuerysetEqual(
            response.context['latest_world_list'],
            ['<World: Past world.>']
        )

    def test_index_view_with_a_future_world(self):
        """ Worlds with a creation_date in the future should not be displayed on
        the index page.
        """
        create_world(name="Future world.", days=30)
        response = self.client.get(reverse('adventure_time:index'))
        self.assertContains(response, "No worlds are available.", status_code=200)
        self.assertQuerysetEqual(response.context['latest_world_list'], [])

    def test_index_view_with_future_world_and_past_world(self):
        """ Even if both past and future worlds exist, only past worlds should
        be displayed.
        """
        create_world(name="Past world.", days=-30)
        create_world(name="Future world.", days=30)
        response = self.client.get(reverse('adventure_time:index'))
        self.assertQuerysetEqual(
            response.context['latest_world_list'],
            ['<World: Past world.>']
        )

    def test_index_view_with_two_past_worlds(self):
        """ The worlds index page may display multiple worlds.
        """
        create_world(name="Past world 1.", days=-30)
        create_world(name="Past world 2.", days=-5)
        response = self.client.get(reverse('adventure_time:index'))
        self.assertQuerysetEqual(
            response.context['latest_world_list'],
            ['<World: Past world 1.>', '<World: Past world 2.>']
        )


class WorldIndexDetailTests(TestCase):

    def test_detail_view_with_a_future_world(self):
        """ The detail view of a world with a creation_date in the future should
        return a 404 not found.
        """
        future_world = create_world(name='Future world.', days=5)
        response = self.client.get(reverse('adventure_time:detail', args=(future_world.id,)))
        self.assertEqual(response.status_code, 404)

    def test_detail_view_with_a_past_world(self):
        """ The detail view of a world with a creation_date in the past should
        display the world's name.
        """
        past_world = create_world(name='Past World.', days=-5)
        response = self.client.get(reverse('adventure_time:detail', args=(past_world.id,)))
        self.assertContains(response, past_world.name, status_code=200)
