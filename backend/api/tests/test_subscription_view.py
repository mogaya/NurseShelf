from .test_setup import SubscriptionTestSetUp
from rest_framework import status
from ..models import Subscription
from django.utils.timezone import now, timedelta

class TestSubscriptionView(SubscriptionTestSetUp):
    def test_admin_can_view_all_subscriptions(self):
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')

        res = self.client.get(self.subscription_url)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(len(res.data), 3)

    def test_user_can_only_view_own_subscriptions(self):
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.regular_access_token}')

        res = self.client.get(self.subscription_url)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(len(res.data), 1)

    def test_user_can_subscribe_to_a_category(self):
        # self.client.logout()
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.regular_access_token}')

        data = {
            'user': self.regular_user.id,
            'category' : self.category2.id,
            # 'end_date' : str(now().date() + timedelta(days = 365.25/2))
        }

        res = self.client.post(self.subscription_url, data, format="json")

        # import pdb
        # pdb.set_trace()

        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Subscription.objects.filter(user=self.regular_user).count(), 3)

    def test_user_cannot_subscribe_twice_to_same_category(self):
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.regular_access_token}')

        data ={
            'user' : self.regular_user.id,
            'category' : self.category1.id
        }

        res = self.client.post(self.subscription_url, data, format='json')
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_user_can_cancel_own_subscription(self):
        self.client.credentials(HTTP_AUTHORIZATION = f'Bearer {self.regular_access_token}')

        res = self.client.post(f'{self.subscription_url}{self.subscription1.id}/cancel/')
        
        # import pdb
        # pdb.set_trace()

        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_user_cannot_cancel_another_users_subscription(self):
        self.client.credentials(HTTP_AUTHORIZATION = f'Bearer {self.regular_access_token}')

        url = f'{self.subscription_url}{self.subscription2.id}/cancel/'

        res = self.client.post(url, format="json")

        # import pdb
        # pdb.set_trace()
        
        self.assertEqual(res.status_code, status.HTTP_404_NOT_FOUND)

    def test_admin_can_cancel_any_subscription(self):
        self.client.credentials(HTTP_AUTHORIZATION = f'Bearer {self.access_token}')

        res = self.client.post(f'{self.subscription_url}{self.subscription1.id}/cancel/')

        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_expired_subscription_is_deactivated(self):
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.regular_access_token}')

        res = self.client.get(self.subscription_url)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(len(res.data), 1)

        self.subscription3.refresh_from_db()
        self.assertFalse(self.subscription3.is_active)


"""
What These Tests Verify
 - Admins can view all subscriptions 
    (test_admin_can_view_all_subscriptions).
 - Users can only view their own subscriptions 
    (test_user_can_only_view_own_subscriptions).
 - Users can subscribe to a new category 
    (test_user_can_subscribe_to_a_category).
 - Users cannot subscribe twice to the same category 
    (test_user_cannot_subscribe_twice_to_same_category).
 - Users can cancel their own subscription 
    (test_user_can_cancel_own_subscription).
 - Users cannot cancel other users' subscriptions 
    (test_user_cannot_cancel_another_users_subscription).
 - Admins can cancel any subscription 
    (test_admin_can_cancel_any_subscription).
 - Test that expired subscriptions are deactivated automatically
    (test_expired_subscription_is_deactivated)
"""