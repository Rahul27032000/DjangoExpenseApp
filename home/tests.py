from django.test import TestCase
from django.contrib.auth.models import User
from .models import Profile, Expense

class ProfileModelTestCase(TestCase):
    def setUp(self):
        # Create a user and a profile for testing
        self.user = User.objects.create_user(username="testuser", password="testpassword")
        self.profile = Profile.objects.create(user=self.user, income=1000.0)

    def test_balance_calculation(self):
        # Ensure that the balance is calculated correctly
        self.assertEqual(self.profile.balance, 1000.0)

class ExpenseModelTestCase(TestCase):
    def setUp(self):
        # Create a user and an expense for testing
        self.user = User.objects.create_user(username="testuser", password="testpassword")
        self.expense = Expense.objects.create(user=self.user, name="Groceries", amount=50.0, expense_type="Positive")

    def test_expense_creation(self):
        # Ensure that the expense is created with the correct details
        self.assertEqual(self.expense.name, "Groceries")
        self.assertEqual(self.expense.amount, 50.0)
        self.assertEqual(self.expense.expense_type, "Positive")


class ProfileModelTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="testpassword")
        self.profile = Profile.objects.create(user=self.user, income=1000.0)

    def test_balance_calculation(self):
        self.assertEqual(self.profile.balance, 1000.0)

    def test_income_default_value(self):
        profile = Profile.objects.create(user=self.user,income=1000.0)
        self.assertEqual(profile.income, 1000.0)

    def test_expenses_default_value(self):
        profile = Profile.objects.create(user=self.user,income=1000.0)
        self.assertEqual(profile.expenses, 0.0)

    def test_profile_str_method(self):
        self.assertEqual(str(self.profile), self.user.username)
