t = int(input())

for _ in range(t):  
    floor = int(input())  # ��
    num = int(input())  # ȣ
    f0 = [x for x in range(1, num+1)]  # 0�� ����Ʈ
    for k in range(floor):  # �� �� ��ŭ �ݺ�
        for i in range(1, num):  # 1 ~ n-1���� (�ε����� ���)
            f0[i] += f0[i-1]  # ���� �� ȣ���� ��� ���� ����
    print(f0[-1])  # ���� ������ �� ���