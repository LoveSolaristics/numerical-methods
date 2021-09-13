import streamlit as st
from methods.chord_method import chord_method_visualization
from methods.dichotomy import dichotomy_visualization
from methods.gradient_descent import gradient_descent_visualization
from methods.jacobi_method import jacobi_method_visualization

from pathlib import Path
import base64


def img_to_bytes(img_path):
    img_bytes = Path(img_path).read_bytes()
    encoded = base64.b64encode(img_bytes).decode()
    return encoded


st.set_page_config(
    page_title="Калькуляторы", layout="wide", initial_sidebar_state="expanded"
)

st.sidebar.markdown("""# Онлайн-калькуляторы""")

# Выбор задачи

tasks_list = ['Решение систем линейных уравнений',
              'Решение нелинейных уравнений',
              'Решение систем нелинейных уравнений']

task = st.sidebar.selectbox("Задача", tasks_list)

if task == tasks_list[0]:
    method = st.sidebar.info('Задача будет решаться методом Якоби')
    method_code = 0
elif task == task == tasks_list[1]:
    method = st.sidebar.selectbox("Методы решения",
                                  ['Метод дихотомии', 'Метод хорд'])
    method_code = 1 if method == 'Метод дихотомии' else 2
else:
    method = st.sidebar.info(
        'Задача будет решаться методом градиентного спуска')
    method_code = 3

# Дополнительная информация

with st.sidebar:
    st.markdown("## Ресурсы")

    st.markdown(
        """[<img src='data:image/png;base64,{}' class='img-fluid'
        width=32 height=32>]\
        (https://www.python.org) <small>Python 3.8.2 |
         September 2021</small>"""
        .format(img_to_bytes("images/python-logo.png")),
        unsafe_allow_html=True,
    )

    st.markdown(
        """[<img src='data:image/png;base64,{}' class='img-fluid'
         width=32 height=32>]\
        (https://streamlit.io) <small>Streamlit 0.88.0 |
         September 2021</small>"""
        .format(img_to_bytes("images/streamlit-logo.png")),
        unsafe_allow_html=True)

    st.markdown(
        """## Прочее
[<img src='data:image/png;base64,{}' class='img-fluid' width=32 height=32>]\
(https://vk.com/lovesolaristics) <small>Вопросы и предложения</small>"""
        .format(img_to_bytes("images/brain.png")),
        unsafe_allow_html=True)

    st.markdown("""
[<img src='data:image/png;base64,{}' class='img-fluid' width=32 height=32>]\
(https://github.com/LoveSolaristics/numerical-methods)
 <small>Исходный код</small>"""
                .format(img_to_bytes("images/github-logo.png")),
                unsafe_allow_html=True)

# Применение методов

if method_code == 2:
    chord_method_visualization()
elif method_code == 1:
    dichotomy_visualization()
elif method_code == 3:
    gradient_descent_visualization()
else:
    jacobi_method_visualization()
