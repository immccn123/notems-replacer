# -*- coding: utf-8 -*-
'''
    Note.ms Replacer
    Copyright (C) 2023 Imken Luo <me@imken.moe>

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
'''

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys, ActionChains

import time, sys

target = "<link>"

content = "<content>"

wait_time = 1

driver = webdriver.Chrome()
driver.maximize_window()

while True:
    try:
        driver.get('https://note.ms/' + target)
    except:
        continue
    time.sleep(0.5)
    el = driver.find_element(By.CLASS_NAME, 'content')
    if el.text != content:
        wait_time = 3
        ActionChains(driver).click(el)\
            .key_down(cmd_ctrl)\
            .send_keys("a")\
            .key_up(cmd_ctrl)\
            .send_keys(content)\
            .perform()
    else:
        if wait_time <= 32 * 3:
            wait_time *= 1.2
    time.sleep(wait_time)
