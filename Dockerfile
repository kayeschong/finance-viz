FROM python:3.8.2

RUN mkdir -p /root/.streamlit
RUN bash -c 'echo -e "\
[general]\n\
email = \"your-email@domain.com\"\n\
" > /root/.streamlit/credentials.toml'

RUN bash -c 'echo -e "\
[server]\n\
headless = true\n\
enableCORS = false\n\
" > /root/.streamlit/config.toml'

EXPOSE 8501

COPY requirements.txt ./requirements.txt
RUN pip install -r requirements.txt
COPY . .
CMD streamlit run app.py
