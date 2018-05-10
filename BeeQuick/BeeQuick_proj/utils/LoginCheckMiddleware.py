from time import time

from django.http import HttpResponseRedirect
from django.utils.deprecation import MiddlewareMixin
from django.core.urlresolvers import reverse
import re

from users.models import UserModel, TicketModel


# class UserMiddleware(MiddlewareMixin):
#
#     def process_request(self, request):
#
#         path = request.path
#         ticket = request.COOKIES.get('ticket')
#         if (path == '/mine/mine/' or path == '/quickbuy/market/') and not request.user.id and not ticket:
#             return None
#
#         re_patterns = (r'^/user/*', r'^/homepage/*', r'^/quickbuy/market/.+')
#
#         for patt in re_patterns:
#             if re.match(patt, path):
#                 return None
#
#         if not ticket:
#             return HttpResponseRedirect(reverse('user:login', kwargs={'r_path': path}))
#
#         tm = TicketModel.objects.filter(ticket=ticket)
#         if tm:
#             if tm.first().create_time + 3600 < int(time()):
#                 return HttpResponseRedirect(reverse('user:login', kwargs={'r_path': path}))
#         else:
#             return HttpResponseRedirect(reverse('user:login', kwargs={'r_path': path}))
#
#         request.user = tm.first().user


class UserMiddleware(MiddlewareMixin):

    def process_request(self, request):

        path = request.path
        ticket = request.COOKIES.get('ticket')

        if not ticket:
            pass
        else:
            tm = TicketModel.objects.filter(ticket=ticket)
            if tm:
                if tm.first().create_time + 3600 < int(time()):
                    pass
                else:
                    request.user = tm[0].user
