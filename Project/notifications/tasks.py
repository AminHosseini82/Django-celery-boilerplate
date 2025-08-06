from celery import shared_task
import time


@shared_task
def count_words():
    time.sleep(5)  # شبیه‌سازی یک کار زمان‌بر
    return


@shared_task
def count_sentences():
    time.sleep(5)  # شبیه‌سازی یک کار زمان‌بر
    return


@shared_task
def find_longest_word():
    time.sleep(5)  # شبیه‌سازی یک کار زمان‌بر
    return
