# Pure Python Game Script Frame
base `minidevice` and `minicv`
- Template
    - ImageTemplate
    - MultiColorsTemplate
- GameScript
    - screenshot -> cv2.Mat
    - find(Template,isColor=None,colorThreshold=4)
    - findAndOperate(Template,operate,operateParams)
    - rangeRandomClick(result,duration,randomPointGenerateAlgo)
    - curveSwipe(startX,startY,endX,endY,duration,curveGenerateAlgo)
    - click(x,y,duration)
    - swipe(points,duration)
    - screenshot_raw()
    - save_screenshot(path)