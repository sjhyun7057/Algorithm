def solution(new_id):
    
    def first(new_id): # 1단계 소문자로 바꾸기
        return new_id.lower()
    
    def second_third(new_id): # 2단계 알파벳 소문자, 숫자, -, _, .를 제외한 모든 문자를 제거
        # 3단계 .이 연속되면 1개의 .로 치환
        # 4단계-1 처음에 .이 올 경우 제거 
        possible_ord = [ord('.'), ord('_'), ord('-')] # 가능한 특수문자
        check_comma = 0 # .이 연속되는지 확인
        a_new_id = '' # 새로 받을 빈 문자열
        for a in first(new_id):
            if 48<=ord(a)<=57 or 97<=ord(a)<=122 or ord(a) in possible_ord:
                if not a_new_id and a == '.': # 만약 문자열이 비었을때 처음이 .이라면 안받음
                    continue
                if check_comma and a == '.': # 이전에 문자가 .이라면 안받음
                    continue
                a_new_id += a
                if a == '.': # . 일경우 check_comma를 1로 바꿈(이전 문자열확인용도)
                    check_comma = 1
                else:
                    check_comma = 0
            else:
                pass
        return a_new_id
    def fourth_fifth(new_id):
        # 4단계-2 끝에 . 일경우 제거
        # 5단계 빈문자열일 경우 'a'로 바꿔줌
        new_id = second_third(new_id)
        if not new_id:
            new_id = 'a'
            return new_id
        idx = len(new_id)
        for a in range(len(new_id)-1,-1,-1): # 뒤에서부터 for문을 돔
            if new_id[a] == '.': # 만약 마지막이 . 일경우 idx - 1
                idx -= 1
            else: # 아닐경우 그만둠
                break
        new_id = new_id[:idx] # 슬라이싱
        return new_id

    def sixth_seventh(new_id):
        # 6단계 길이가 16이상일 경우 15까지 짤라주고 마지막에 .이 있을경우 제거
        # 7단계 3이하일 경우 그 이전의 문자로 채워넣음
        new_id = fourth_fifth(new_id)
        length_id = len(new_id)
        if length_id > 15:
            new_id = fourth_fifth(new_id[:15]) # 15까지 슬라이싱을하고 4단계함수에 리턴
        else:
            if length_id < 3:
                while length_id < 3:
                    new_id += new_id[-1]
                    length_id += 1
        return new_id
    
    new_id = sixth_seventh(new_id)
        
    return new_id