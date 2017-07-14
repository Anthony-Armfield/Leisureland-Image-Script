count = 1

with open('G:\Work Stuff\Technode\LeisurelandRVCenter\Python Programs\image_script.txt', 'w') as dest:
    while count < 52:
        imageString1 = '{"id":"'
        imageString10 = imageString1 + str(count)
        imageString2 = '","title":"","description":"","url":"..\/..\/data\/imagegallery\/2005-skyline-layton-rampage-289\/'
        imageString20 = imageString2 + str(count)
        imageString3 = '.jpeg","thumbUrl":"..\/..\/data\/imagegallery\/2005-skyline-layton-rampage-289\/'
        imageString30 = imageString3 + str(count)
        imageString4 = '.thumb.jpeg"},'
        imageString40 = imageString4
        dest.write ('%s%s%s%s' % (imageString10,imageString20,imageString30,imageString40))
        count = count + 1
