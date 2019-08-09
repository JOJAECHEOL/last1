from django.shortcuts import render, get_object_or_404
from loginapp.models import Member
from backapp.models import Goods

def index(request):
    return render(request, 'light_main.html')

def oneselection(request):
    other = Member.objects.get(id=1)
    a=''
    a = other.choose
    all = ['캘리그라피','뜨개질','스티커 아트', '미니 레고', '생활 보드','실 팔찌 만들기','배드민턴']
    all.remove(a)
    
    return render(request, 'one_selection.html',{'all':all})

def twoselection(request):
    return render(request, 'two_selection.html')

def threeselection(request):
    return render(request, 'three_selection.html')

def mypage(request):
    return render(request, 'mypage.html')

def buy(request):
    other = Member.objects.get(id=1)
    a=''
    a = other.choose
    goods = Goods.objects.all().filter().exclude(item__contains=a)
    return render(request, 'buy.html',{'goods':goods})

def buy3(request, item_id):
    item=[]
    for k in item_id:
        if k.isdigit():
            item.append(int(k))
        else:
            continue
    count = 4   #ㅎㅇ연지야 코드를 더렵혀서 미안#
    idrandom=[] #그만울고 위에 for문은 '[1,2,3,4,5]' 이모양 int로 구성된 list로 바꾼거고
                #밑에는 randomsamle값이 list인데 연지가 list안에 넣어서 [[1,2,3,5]] 모양이라서 에러였음
    idrandom = random.sample(item, count)#테스트 해볼라니까 뭔가 내가 알고있는 data가 없어서 못하겠움
    
    buy = Goods.objects.filter(id__in=idrandom)
    return render(request, 'buy3.html', {"buy": buy})

# def detail(request, light_id):
#     light_detail = get_object_or_404(Light, pk=light_id)
#     return render(request, 'detail.html', {'light':light_detail})
