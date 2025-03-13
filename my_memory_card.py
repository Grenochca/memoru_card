from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget, QHBoxLayout, QVBoxLayout, QGroupBox, QRadioButton, QPushButton, QLabel, QButtonGroup)
from random import shuffle

class Question():
    def __init__(self,q,right_answer,wrong1,wrong2,wrong3):
        self.q = q
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

questions_list = [] 
questions_list.append(Question('Государственный язык Бразилии', 'Португальский', 'Английский', 'Испанский', 'Бразильский'))
questions_list.append(Question('Какого цвета нет на флаге России?', 'Зелёный', 'Красный', 'Белый', 'Синий'))
questions_list.append(Question('Национальная хижина якутов', 'Ураса', 'Юрта', 'Иглу', 'Хата'))


app = QApplication([])
main_win = QWidget()
main_win.setWindowTitle('Memory Card')
queustion = QLabel('гшщпт3т')
btn_ok = QPushButton('ответить')
RadioGrupBox = QGroupBox('Варианты атветов')
rbtn1 = QRadioButton('Энцы')
rbtn2 = QRadioButton('Чулымцы')
rbtn3 = QRadioButton('Смурфы')
rbtn4 = QRadioButton('Алеуты')
RadioGroup = QButtonGroup() 
RadioGroup.addButton(rbtn1)
RadioGroup.addButton(rbtn2)
RadioGroup.addButton(rbtn3)
RadioGroup.addButton(rbtn4)

layout_ans1 = QHBoxLayout()
layout_ans2 = QVBoxLayout()
layout_ans3 = QVBoxLayout()

layout_ans2.addWidget(rbtn1)
layout_ans2.addWidget(rbtn2)
layout_ans3.addWidget(rbtn3)
layout_ans3.addWidget(rbtn4)
layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)

RadioGrupBox.setLayout(layout_ans1)

AnsGrupBox = QGroupBox('результат теста')
result = QLabel('Правильно/Непрвильно')
correct = QLabel('Правилный ответ')
layout_res = QVBoxLayout()
layout_res.addWidget(result, alignment=(Qt.AlignLeft | Qt.AlignTop))
layout_res.addWidget(correct, alignment=Qt.AlignHCenter, stretch=2)

AnsGrupBox.setLayout(layout_res)

layout1 = QHBoxLayout()
layout2 = QHBoxLayout()
layout3 = QHBoxLayout()

layout1.addWidget(queustion, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))
layout2.addWidget(RadioGrupBox)
layout2.addWidget(AnsGrupBox)
layout3.addStretch(1)
layout3.addWidget(btn_ok, stretch=2)
layout3.addStretch(1)
layout_main = QVBoxLayout()
layout_main.addLayout(layout1)
layout_main.addLayout(layout2)
AnsGrupBox.hide()
def show_result():
    RadioGrupBox.hide()
    AnsGrupBox.show()
    btn_ok.setText('Следующий вопрос')
def show_queustion():
    RadioGrupBox.show()
    AnsGrupBox.hide()
    btn_ok.setText('ответить')  
    RadioGroup.setExclusive(False)
    rbtn1.setChecked(False)
    rbtn2.setChecked(False)
    rbtn3.setChecked(False)
    rbtn4.setChecked(False)
    RadioGroup.setExclusive(True)

answers = [rbtn1, rbtn2, rbtn3, rbtn4]
def ask(q):
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    queustion.setText(q.q)
    correct.setText(q.right_answer) 
    show_queustion()
def show_correct(res):
    result.setText(res)
    show_result()
def check_answer():
    if answers[0].isChecked():
        show_correct('Правильно!')
    else:
        if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
            show_correct('Неверно!')
def next_question():
    main_win.cur_question +=1
    if main_win.cur_question >=len(questions_list):
        main_win.cur_question =0
    ask(questions_list[main_win.cur_question])
def click_ok():
    if btn_ok.text() =='ответить':
        check_answer()
    else:
        next_question()

main_win.cur_question =-1
btn_ok.clicked.connect(click_ok)
next_question()
layout_main.addLayout(layout3)
main_win.setLayout(layout_main)
main_win.show()
app.exec()

