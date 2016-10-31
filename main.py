# -*- coding: utf-8 -*-
import service
import adsl

# trainService = service.TrainOrderService({})

adsl_service = adsl.Adsl()
adsl_service.set_adsl({"name": u"宽带连接",
                       "username": "0512...",
                       "password": "..."})

