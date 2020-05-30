import scrapy
from ..items import DemoItem
from ..file1 import *
import matplotlib
import matplotlib.pyplot as plt

class firstWeb(scrapy.Spider):
    name='myspider'
    start_urls=['https://www.mygov.in/covid-19'
                ]
    page_no=2
    def parse(self, response):

        items=DemoItem()

        state_name=response.css(".st_name::text").extract()
        confirmed=response.css(".tick-confirmed small::text").extract()
        active=response.css(".tick-active small::text").extract()
        recovered=response.css(".tick-discharged small::text").extract()
        death=response.css(".tick-death small::text").extract()


        items['state_name']=state_name
        items['confirmed']=confirmed
        items['active']=active
        items['recovered']=recovered
        items['death']=death

        yield items
        for i in range(len(state_name)):
            if state_name[i]=='Uttar Pradesh':
                state_name[i]='U.P'

        index=[9,11,15,17,21,28,29,31,34,36]

        plt_name=[state_name[i] for i in index]
        plt_conf=[int(confirmed[i]) for i in index]
        plt_recovered = [int(recovered[i]) for i in index]
        plt_death=[int(death[i]) for i in index]

        plot_bar(plt_name,plt_conf)
        plot_bar(plt_name,plt_recovered,w=0.5,c1='g')
        plot_bar(plt_name, plt_death, w=0.3,c1='r')
        plt.show()

        df=pd.DataFrame({'State_Name':state_name,'Confirmed_Cases':confirmed,'Active_case':active,'Recovered_Cases':recovered,'Death_Cases':death})
        store(df)























