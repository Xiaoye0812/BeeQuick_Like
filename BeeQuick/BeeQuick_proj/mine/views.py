from django.shortcuts import render


def mine(request):

    if request.method == 'GET':
        user = request.user
        try:
            orders = user.ordermodel_set.all()
        except:
            pay_num = 0
            wait_num = 0
        else:
            pay_num = len(orders.filter(o_status=0))
            wait_num = len(orders.filter(o_status=1))

        return render(request, 'mine/mine.html', {'pay_num': pay_num, 'wait_num': wait_num})
