transform center_lower:
    xalign 0.5           # 水平中央
    yalign 1.015          # 比 1.0 稍高（偏下但留一点空隙）
    zoom 0.9             # 缩小 10%
    xanchor 0.5          # 锚点居中，确保缩放时以中心为基准
    yanchor 1.0          # 锚点底部，确保脚底对齐

    yoffset 0            # 起始位置，垂直偏移为0
    linear 2.0 yoffset -10 # 在2秒内线性移动到向上偏移10像素的位置
    linear 2.0 yoffset 0 # 在2秒内线性移动回垂直偏移为0的位置
    repeat               # 重复以上动作

transform center7:

    xalign 0.5           # 水平中央
    yalign 1.05  
    zoom 0.55        # 比 1.0 稍高（偏下但留一点空隙）             
    xanchor 0.5          # 锚点居中，确保缩放时以中心为基准
    yanchor 1.0          # 锚点底部，确保脚底对齐

    yoffset 0            # 起始位置，垂直偏移为0
    linear 2.0 yoffset -10 # 在2秒内线性移动到向上偏移10像素的位置
    linear 2.0 yoffset 0 # 在2秒内线性移动回垂直偏移为0的位置
    repeat               # 重复以上动作


transform zom:
    xalign 0.5           # 水平中央
    yalign 1.05  
    zoom 0.27        # 比 1.0 稍高（偏下但留一点空隙）             
    xanchor 0.5          # 锚点居中，确保缩放时以中心为基准
    yanchor 1.0          # 锚点底部，确保脚底对齐

    yoffset 0            # 起始位置，垂直偏移为0
    linear 2.0 yoffset -10 # 在2秒内线性移动到向上偏移10像素的位置
    linear 2.0 yoffset 0 # 在2秒内线性移动回垂直偏移为0的位置
    repeat               # 重复以上动作


transform bg_zoom_out1:
    zoom 0.25
    xalign 0.5
    yalign 0.5

transform bg_zoom_out2:
    zoom 0.5
    xalign 0.5
    yalign 0.5

define fast_dissolve = Dissolve(0.3)