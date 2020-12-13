from django.shortcuts import render
from django.http import HttpResponse
from django .shortcuts import redirect
from django.views.generic import TemplateView
import random
from .models import QuestionnaireAnswerModel
#from .forms import QuestionnaireAnswerForm

# Create your views here.
def index(request):
    return HttpResponse('survey')

class Survey(TemplateView):

    def __init__(self):
        #アンケート項目
        survey_list = [
            '乗り心地',
            '荷室の使いやすさ',
            '燃費の良さ',
            '排気量の少なさ',
            '車内空間が広い',
            '静かに走る',
            '馬力がある',
            '乗車定員が多い',
            '小回りが利く',
            '乗り降りしやすい',
            '安全性能が高い',
            '走行性能が高い',
            '車両サイズが小さい',
            'カスタムしやすい',
            'オプションが充実してる',
        ]
        #survey_listの中からランダムに5つ選ぶ
        rsl = random.sample(survey_list, 5)
        print(rsl)
        self.params = {
            'title': 'アンケート',
            'message': '車選びで重視するものを選択してください',
            'data': rsl,
            'list': survey_list
        }

    def get(self, request):
        blank_list = []
        test_list = QuestionnaireAnswerModel.objects.filter(user_id=request.session['user_id'])
        sample_list = test_list.values('answer_1','answer_2','answer_3','answer_4','answer_5',\
        'answer_6','answer_7','answer_8','answer_9','answer_10',\
        'answer_11','answer_12','answer_13','answer_14','answer_15')
        index_list = sample_list[0]
        for k, v in index_list.items():
            if v == '':
                blank_list.append(k)
        print(blank_list)
        new_survey_list = []
        survey_dict = {
            'answer_1': '乗り心地',
            'answer_2': '荷室の使いやすさ',
            'answer_3': '燃費の良さ',
            'answer_4': '排気量の少なさ',
            'answer_5': '車内空間が広い',
            'answer_6': '静かに走る',
            'answer_7': '馬力がある',
            'answer_8': '乗車定員が多い',
            'answer_9': '小回りが利く',
            'answer_10': '乗り降りしやすい',
            'answer_11': '安全性能が高い',
            'answer_12': '走行性能が高い',
            'answer_13': '車両サイズが小さい',
            'answer_14': 'カスタムしやすい',
            'answer_15': 'オプションが充実してる',
        }
        for answer_number in blank_list:
            for k, v in survey_dict.items():
                if answer_number == k:
                    new_survey_list.append(v)
        print(new_survey_list)
        rsl = random.sample(new_survey_list, 5)
        print(rsl)
        self.params = {
            'title': 'アンケート',
            'message': '車選びで重視するものを選択してください',
            'data': rsl,
            'list': new_survey_list
        }
        return render(request, 'survey/questionnaire.html', self.params)

    def post(self, request):
        #コンストラクタ（__init__）でrandom関数をかけて選択されたrslをセッションに代入しておき、再度表示 -> checks_valueに含まれているかどうか判別
        input_rsl = request.POST.getlist("rsl_data")
        input_list = request.POST.getlist("rsl_list")
        request.session['base_rsl'] = input_rsl
        request.session['new_rsl'] = input_list
        print(request.session['base_rsl'])
        print(request.session['new_rsl'])

        #チェックされたアンケート項目を取得
        checks_value = request.POST.getlist('checks[]')
        print(checks_value)
        #取得したアンケート項目を仕分けして適切な位置に保存(試行錯誤中)
        rsl_list = request.session['base_rsl']
        survey_list = request.session['new_rsl']
        matched_list = []
        for item in rsl_list:
            for data in survey_list:
                if item == data:
                    survey_list.remove(item)
        print(survey_list)
        for item in rsl_list:
            for index in checks_value:
                if item == index:
                    matched_list.append(item)
                    rsl_list.remove(item)
                    break
        print(matched_list)
        print(rsl_list)
                        
        for item in matched_list:
            if item == '乗り心地':
                answer_1 = 1
            elif item == '荷室の使いやすさ':
                answer_2 = 1
            elif item == '燃費の良さ':
                answer_3 = 1
            elif item == '排気量の少なさ':
                answer_4 = 1
            elif item == '車内空間が広い':
                answer_5 = 1
            elif item == '静かに走る':
                answer_6 = 1
            elif item == '馬力がある':
                answer_7 = 1
            elif item == '乗車定員が多い':
                answer_8 = 1
            elif item == '小回りが利く':
                answer_9 = 1
            elif item == '乗り降りしやすい':
                answer_10 = 1
            elif item == '安全性能が高い':
                answer_11 = 1
            elif item == '走行性能が高い':
                answer_12 = 1
            elif item == '車両サイズが小さい':
                answer_13 = 1
            elif item == 'カスタムしやすい':
                answer_14 = 1
            elif item == 'オプションが充実してる':
                answer_15 = 1

        for item in rsl_list:
            if item == '乗り心地':
                answer_1 = 0
            elif item == '荷室の使いやすさ':
                answer_2 = 0
            elif item == '燃費の良さ':
                answer_3 = 0
            elif item == '排気量の少なさ':
                answer_4 = 0
            elif item == '車内空間が広い':
                answer_5 = 0
            elif item == '静かに走る':
                answer_6 = 0
            elif item == '馬力がある':
                answer_7 = 0
            elif item == '乗車定員が多い':
                answer_8 = 0
            elif item == '小回りが利く':
                answer_9 = 0
            elif item == '乗り降りしやすい':
                answer_10 = 0
            elif item == '安全性能が高い':
                answer_11 = 0
            elif item == '走行性能が高い':
                answer_12 = 0
            elif item == '車両サイズが小さい':
                answer_13 = 0
            elif item == 'カスタムしやすい':
                answer_14 = 0
            elif item == 'オプションが充実してる':
                answer_15 = 0

        for item in survey_list:
            if item == '乗り心地':
                answer_1 = ''
            elif item == '荷室の使いやすさ':
                answer_2 = ''
            elif item == '燃費の良さ':
                answer_3 = ''
            elif item == '排気量の少なさ':
                answer_4 = ''
            elif item == '車内空間が広い':
                answer_5 = ''
            elif item == '静かに走る':
                answer_6 = ''
            elif item == '馬力がある':
                answer_7 = ''
            elif item == '乗車定員が多い':
                answer_8 = ''
            elif item == '小回りが利く':
                answer_9 = ''
            elif item == '乗り降りしやすい':
                answer_10 = ''
            elif item == '安全性能が高い':
                answer_11 = ''
            elif item == '走行性能が高い':
                answer_12 = ''
            elif item == '車両サイズが小さい':
                answer_13 = ''
            elif item == 'カスタムしやすい':
                answer_14 = ''
            elif item == 'オプションが充実してる':
                answer_15 = ''
        
        user_id = request.session['user_id'] 

        record = QuestionnaireAnswerModel(user_id = user_id, answer_1 = answer_1, answer_2= answer_2, answer_3 = answer_3, answer_4= answer_4, answer_5 = answer_5, \
            answer_6 = answer_6, answer_7 = answer_7, answer_8 = answer_8, answer_9 = answer_9, answer_10 = answer_10, \
            answer_11 = answer_11, answer_12 = answer_12, answer_13 = answer_13, answer_14 = answer_14, answer_15 = answer_15)
        record.save()    
        return render(request, 'survey/questionnaire.html', self.params)         