# 正确率(Precision) = 正确识别的词数 / 识别出的个体总数
#
# 召回率(Recall) = 正确识别的个体总数 / 测试集中存在的个体总数
#
# F值 = 正确率 * 召回率 * 2 / (正确率 + 召回率)


def get_string(list):
    res = ""
    for item in list:
        res = res + item
    return res


def evaluate(out_words, correct_words):
    num_correct = 0
    num_out = len(out_words)
    num_test = len(correct_words)
    i = 0
    j = 0
    while i < len(out_words) and j < len(correct_words):
        if out_words[i] == correct_words[j]:
            num_correct += 1
            i += 1
            j += 1
        else:
            offset_i = offset_j = 1
            while i + offset_i < len(out_words):
                offset_j = 1
                while j + offset_j < len(correct_words):
                    if get_string(out_words[i:i + offset_i]) == get_string(correct_words[j:j + offset_j]):
                        break
                    offset_j += 1
                if get_string(out_words[i:i + offset_i]) == get_string(correct_words[j:j + offset_j]):
                    break
                offset_i += 1
            i += offset_i
            j += offset_j
    return num_correct, num_out, num_test


if __name__ == "__main__":
    fin_out = open("./data.out.txt", "r")
    fin = open("./data.conll", "r")

    num_correct = 0
    num_out = 0
    num_test = 0

    while True:
        line_out = fin_out.readline()
        if not line_out:
            break
        out_words = line_out[:-1].split()
        correct_words = []

        while True:
            line = fin.readline()
            if line == "\n":
                break
            correct_words.append(line.split()[1])

        res = evaluate(out_words, correct_words)
        num_correct += res[0]
        num_out += res[1]
        num_test += res[2]

    precision = num_correct / float(num_out)
    recall = num_correct / float(num_test)
    F = precision * recall * 2 / (precision + recall)

    fin_out.close()
    fin.close()
