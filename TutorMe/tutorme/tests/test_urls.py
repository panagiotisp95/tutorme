from django.test import SimpleTestCase
from django.urls import reverse, resolve
from tutorme.views import index, about, register_student, register_teacher, user_login, user_logout, search, dashboard, accept, rate

class TestUrls(SimpleTestCase):

    def test_index_url_resolves(self):
        url = reverse('index')
        print(resolve(url))
        self.assertEquals(resolve(url).func, index)

    def test_about_url_resolves(self):
        url = reverse('about')
        print(resolve(url))
        self.assertEquals(resolve(url).func, about)


    def test_register_student_url_resolves(self):
        url = reverse('register_student')
        print(resolve(url))
        self.assertEquals(resolve(url).func, register_student)


    def test_register_teacher_url_resolves(self):
        url = reverse('register_teacher')
        print(resolve(url))
        self.assertEquals(resolve(url).func, register_teacher)

    def test_login_url_resolves(self):
        url = reverse('login')
        print(resolve(url))
        self.assertEquals(resolve(url).func, login)

    def test_logout_url_resolves(self):
        url = reverse('logout')
        print(resolve(url))
        self.assertEquals(resolve(url).func, logout)

    def test_search_url_resolves(self):
        url = reverse('search')
        print(resolve(url))
        self.assertEquals(resolve(url).func, search)

    def test_dashboard_url_resolves(self):
        url = reverse('dashboard')
        print(resolve(url))
        self.assertEquals(resolve(url).func, dashboard)

    def test_accept_url_resolves(self):
        url = reverse('accept')
        print(resolve(url))
        self.assertEquals(resolve(url).func, accept)

    def test_rate_url_resolves(self):
        url = reverse('rate')
        print(resolve(url))
        self.assertEquals(resolve(url).func, rate)