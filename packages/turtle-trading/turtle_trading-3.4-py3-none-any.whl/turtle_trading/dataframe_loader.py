#!/usr/bin/env python
# -*- coding: utf8 -*-
""" initialize a dataframe """
import warnings
import datetime
# import pandas as pd
from typing import Optional

from yahoo_fin.stock_info import get_data, get_live_price

""" ignore Pandas Future Warning and SettingWithCopyWarnings """
warnings.simplefilter(action='ignore', category=FutureWarning)


class DataFrameLoader:
  """This class builds the pd.DataFrame used for turtle_trading functionalities. 

  :param ticker: A ticker symbol.
  :param type: Optional, stock or futures.
  """
  def __init__(self, ticker: str, type: Optional[str] = "futures"):
    self.ticker = ticker.upper()
    if type is not ("futures", "stock"):
      raise ValueError(f"invalid type: {type}")
    
    self.type = type
    self.dataframe = self.__initalize(type)
    self.base_dataframe = self.dataframe # back up 


  def __initalize(self, type):
    """ initialize dataframe """
    if type == "futures":
      # query.py
      pass 
    
    dataframe = get_data(self.ticker, interval='1d')
    return dataframe
  
  def edit_columns(self, columns: list[str]):
    """ get specific columns """
    self.dataframe = self.dataframe[columns]
    return self.dataframe
  
  def reverse(self):
    """ reverse dataframe """
    self.dataframe = self.dataframe.iloc[::-1]
    return self.dataframe
  
  def start_at(self, date: datetime.date):
    """ start dataframe at a location """
    self.dataframe = self.dataframe[date:]
    return self.dataframe
  
  @property
  def live_price(self):
    """ get live price """
    return get_live_price(self.ticker)

  
  def reset(self):
    """ reset dataframe """
    self.dataframe = self.base_dataframe
    return self.dataframe
  
  def get_price(self, date: datetime.date): 
    """ get price based on date """
    if str(self.dataframe.iloc[0].name).split("-")[0] != str(datetime.datetime.now().year):
      # will work if ticker became public before current year, else will not work
      self.reverse()
    
    return self.start_at(date).iloc[0]['close']