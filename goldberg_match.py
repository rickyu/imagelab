#encoding: utf-8

from image_match.goldberg import ImageSignature

def match(path1, path2):
    gis = ImageSignature()
    a = gis.generate_signature(path1)
    b = gis.generate_signature(path2)
    return gis.normalized_distance(a, b)

def main():
    
    path1='http://s3.mogucdn.com/mlcdn/c45406/170919_46fbhijglea23d4425hifli9gjj4l_640x960.jpg_468x468.jpg'
    path1_small='http://s3.mogucdn.com/mlcdn/c45406/170919_46fbhijglea23d4425hifli9gjj4l_640x960.jpg_100x100.jpg'
    path2='http://s11.mogucdn.com/mlcdn/c45406/170919_3ahe45ifkaadlhehg8j8dcgfjd830_640x960.jpg_468x468.jpg'
    print(match(path1, path2))
    print(match(path1, path1))
    print(match(path1, path1_small))

if __name__ == '__main__':
    main()    
