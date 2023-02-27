import random


        
    
    
    

def Dou_Lottery(lottery_type=None):
    present_act = random.choice(["喝了二两小熊陈酿","开动了小脑筋","抓破了老戴","使出了吃奶的劲","使用了豆之念力","求助了母星豆之族长","在梦中吐出了一串号码","通过窃取时间宝石","胡乱说了一串号码","灵光一闪","打了个喷嚏","跳了一支神秘的舞蹈","扔了几次骰子","认真研究了上下5000年的走势图","突然发出让人难以理解的怪笑","通过数自己头顶上的毛的数量"])
    if lottery_type == "豆豆大乐透":
        num_name = '前区后区'
        # 前区号码
        front_balls = list(range(1,36))         # 1~35的全部前区球列表
        random.shuffle(front_balls)             # 把列表随机排序
        part1_num = sorted(front_balls[0:5])    # 从列表中取前5个数作为前区号码
        # 后区号码
        behind_balls = list(range(1,13))        # 1~12的全部后区球列表
        random.shuffle(behind_balls)            # 把列表随机排序
        part2_num = sorted(behind_balls[0:2])   # 从列表中取前2个数作为后区号码
        # 分别返回两组号码
    elif lottery_type == "豆豆双色球":
        num_name = '红球蓝球'
        # 红球号码
        red_balls = list(range(1,34))           # 1~33的全部红球列表
        random.shuffle(red_balls)               # 把列表随机排序
        part1_num = sorted(red_balls[0:6])      # 从列表中取前6个数作为红球号码
        # 蓝球号码
        part2_num = random.randint(1,16)        # 从1~16中随机取一个数作为蓝球号码
        # 分别返回两组号码
    str_result = f'═══ 💰{lottery_type.replace("豆豆","")}💰 ═══'
    str_result += f'\n\n豆豆{present_act}，为您做出如下推荐：'
    str_result += f'\n\n🔲{num_name[0:2]}：{part1_num}\n🔲{num_name[2:4]}：{part2_num}'.replace('[','').replace(']','')
    str_result += '\n\n════════════\n本功能仅供娱乐\n最终解释权归豆豆所有'
    return(str_result)