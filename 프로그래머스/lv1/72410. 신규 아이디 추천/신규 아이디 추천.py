new_id = "..ab...cdef.....ghijklmn.p"
def solution(new_id):
    
    def first(new_id):
        return new_id.lower()
    
    def second_third(new_id):
        possible_ord = [ord('.'), ord('_'), ord('-')]
        check_comma = 0
        a_new_id = ''
        for a in first(new_id):
            if 48<=ord(a)<=57 or 97<=ord(a)<=122 or ord(a) in possible_ord:
                if not a_new_id and a == '.':
                    continue
                if check_comma and a == '.':
                    continue
                a_new_id += a
                if a == '.':
                    check_comma = 1
                else:
                    check_comma = 0
            else:
                pass
        return a_new_id
    def fourth_fifth(new_id):
        new_id = second_third(new_id)
        if not new_id:
            new_id = 'a'
            return new_id
        idx = len(new_id)
        for a in range(len(new_id)-1,-1,-1):
            if new_id[a] == '.':
                idx -= 1
            else:
                break
        new_id = new_id[:idx]
        return new_id

    def sixth_seventh(new_id):
        new_id = fourth_fifth(new_id)
        length_id = len(new_id)
        if length_id > 15:
            new_id = fourth_fifth(new_id[:15])
        else:
            if length_id < 3:
                while length_id < 3:
                    new_id += new_id[-1]
                    length_id += 1
        return new_id
    
    new_id = sixth_seventh(new_id)
        
    return new_id
