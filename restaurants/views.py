from django.shortcuts import render

def welcome(request):
    return render(request, 'index.html', {'msg':'Hello World!'})

def restaurant_list(request):

    context = {'my_list':[{'restaurant_name':'Pizza Express', 'food_type':'pizza'}, {'restaurant_name':'KFC', 'food_type':'fast_food'}, {'restaurant_name':'Sakura', 'food_type':'japanese'}],

    }
    return render(request, 'list.html', context)


def restaurant_detail(request):

    context = {'my_object':{'restaurant_name':'shawarma', 'food_type':'Lebnanese'}

    }
    return render(request, 'detail.html', context)
