#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 用于处理与文字相关的逻辑

from random import choice


def word(language):
    '''从文字列表中随机选择一条并返回'''

    word_list_zh = [
        # 神隐少女
        "人生就是一列开往坟墓的列车，路途上会有很多站，很难有人可以自始至终陪着走完。当陪你的人要下车时，即使不舍也该心存感激，然后挥手道别。",
        "不管前方的路有多苦，只要走的方向正确，不管多么崎岖不平，都比站在原地更接近幸福。",
        "我只能送你到这里了，剩下的路你要自己走，不要回头。",
        "用善意的心情去理解别人的话，会让世界单纯美好容易。世界如此之大，我却能幸运地遇见一些人。",
        "我不知道将去何方，但我已在路上。",
        # 猫的报恩
        "你不能等待别人来安排你的人生；自己想要的，自己争取。",
        "心只有一颗，别让它沉浸悲伤。",
        "如果你遇到了有点不可思议又让你困扰的事，不妨去探一探究竟。",
        "我始终相信，在这个世界上，一定有另一个自己，在做着我不敢做的事，在过着我想过的生活。",
        "你应该要学着做你自己，面对真实的自我，只要做到这一点你就什么都不用惧怕。",
        # 風之谷
        "好梦向来易醒。",
        "你不能改变命运，但你可以选择原地等待，或是，勇敢面对。",
        "坚强不是面对悲伤不流一滴泪，而是擦干眼泪后微笑着面对以后的生活。",
        # 天空之城
        "有时候，坚持了你最不想干的事情之后，便可得到你最想要的东西。",
        # 魔女宅急便
        "只有一个人在旅行时，才听得到自己的声音，它会告诉你，这世界比想象中的宽阔。",
        "在这个世界上别太依赖任何人，因为当你在黑暗中挣扎时，连你的影子都会离开你。",
        "不要对外表过分在意，心灵才是最重要的。",
        # 名言佳句
        "It's better to light a candle than curse the darkness.",
        # 歌曲
        "你是你本身的傳奇，憑著你志氣會成大器；天公不造美，幾經風浪也是你。",
        "撞進了冰山，捲上了急灣，一秒從未想折返；就望到了，就能望到了，終會踏足這峽灣。",
        "風雨不會沒了期，終於會等到夢寐；全城在變遷，不減你是你。"
    ]

    word_list_en = [
        "Stand on the shoulders of giants",
    ]

    if language == 'en':
        msg = choice(word_list_en)
    else:
        msg = choice(word_list_zh)

    return msg
