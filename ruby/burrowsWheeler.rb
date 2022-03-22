def encode(s)
    strList = []
    for i in 0..(s.length - 1)
        strList << s.split('').rotate(-i).join('')
    end
    strList = strList.sort
    res = ""
    strList.each do |word|
          res += word[-1]
    end
    return [res, strList.index(s)]
end
def decode(s, n)
    #TODO: implement
end