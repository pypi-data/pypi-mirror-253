import os
import datetime
import operator
from functools import reduce
import ast


class ParaTex:
    def __init__(self, leftParas, upParas, blacklist=None, whitelist=None, ignoreP=None):
        r"""
        参数, 参数名, 参数值, 参数值名 都会被转为字符串类型(为了readTableE), 它们都不可为空和None, 不能包括\符号, 以及{}#$%^&_ 防止latex特殊符号出错.
        考虑到转化为字符串, 因此数值型的str参数需要书写标准, 否则可能与数值型参数不相等.
        @param leftParas: [[参数,参数名,(参数值,..),(参数值名,..)],..], 表格从左至右的参数
        @param upParas: [[参数,参数名,(参数值,..),(参数值名,..)],..], 表格从上至下的参数
        @param blacklist: [{参数:(参数值,..),..},..], 冲突时优先级高于白名单, nextParas 会跳过黑名单输出
        @param whitelist: [{参数:(参数值,..),..},..], 只包含空 {} 会使所有参数为非计算
        @param ignoreP: [参数,..], nextParas 不输出的参数, 用于一次计算返回多个值, setParaV_c的内容值c要按照这个参数及其参数值顺序全排列
        """
        assert len(leftParas[0][2]) == len(leftParas[0][3]) > 0, 'leftParas 格式错误(要求%d==%d>0)!' % (
            len(leftParas[0][2]), len(leftParas[0][3]))
        assert len(upParas[0][2]) == len(upParas[0][3]) > 0, 'upParas 格式错误(要求%d==%d>0)!' % (
            len(upParas[0][2]), len(upParas[0][3]))
        # 转化为str
        haveEmpty = [False]
        leftParas = self._allToString(leftParas, haveEmpty)
        assert not haveEmpty[0], 'leftParas 存在空字符串!'
        upParas = self._allToString(upParas, haveEmpty)
        assert not haveEmpty[0], 'upParas 存在空字符串!'
        if blacklist:
            blacklist = self._allToString(blacklist, haveEmpty)
            assert not haveEmpty[0], 'blacklist 存在空字符串!'
        if whitelist:
            whitelist = self._allToString(whitelist, haveEmpty)
            assert not haveEmpty[0], 'whitelist 存在空字符串!'
        if ignoreP:
            ignoreP = self._allToString(ignoreP, haveEmpty)
            assert not haveEmpty[0], 'ignoreP 存在空字符串!'
        # 获得全排列参数
        paras_v = []
        for i in leftParas:
            paras_v.append([i[0], i[2]])
        for i in upParas:
            paras_v.append([i[0], i[2]])
        all_p = self._all_permutation(paras_v)  # 全排列参数
        all_p_v8m = {i: ['', False if whitelist else True] for i in all_p}

        self._leftParas = leftParas
        self._upParas = upParas
        self._paras_v = paras_v  # [[参数,(参数值,..)],..]
        self._paras_v_D = dict(paras_v)  # 用于 setParaV_c, readTableE
        self._all_p = all_p  # [(排列参数),..]
        self._all_p_v8m = all_p_v8m  # {(排列参数):[值,是否计算],..}
        self._index = -1
        self._alreadyP = set()  # 已经 next 过的排列参数, 用于辅助 ignoreP
        self._ignoreP = ignoreP if ignoreP else []  # 用于 setParaV_c 按序输入
        self._ignoreP_s = set(self._ignoreP)  # 用于 nextParas 判断是否去除
        assert len(self._ignoreP_s & set([i[0] for i in paras_v])) == len(self._ignoreP_s), 'ignoreP存在参数不在表中!'

        # 标注白名单
        if whitelist:
            for l_s in whitelist:
                self._list_filter(l_s, True)
        # 标注黑名单
        if blacklist:
            for l_s in blacklist:
                self._list_filter(l_s, False)

    def _allToString(self, x, haveEmpty: list = None, sfs=True):
        '''
        将非 tuple, list, set, dict 类型递归转为 str 类型, 除了 None.
        @param x: tuple|list|set|dict|str|int|float|bool|None
        @param haveEmpty: list, haveEmpty[0] 表示是否包含空字符串
        @param sfs: bool, 是否将str转float再转str, 可以部分防止因为str中数字多写.或0之类导致不相等, 但是如果故意想不相等反而导致反效果
        @return: tuple|list|set|dict|str|int|float|bool|None
        '''
        if isinstance(x, tuple) or isinstance(x, list) or isinstance(x, set):
            y = []
            for i in x:
                y.append(self._allToString(i, haveEmpty))
            if isinstance(x, tuple):
                y = tuple(y)
            if isinstance(x, set):
                y = set(y)
            return y
        elif isinstance(x, dict):
            y = {}
            for k, v in x.items():
                y[self._allToString(k, haveEmpty)] = self._allToString(v, haveEmpty)
            return y
        elif x is None:
            return None
        else:
            if sfs and isinstance(x, str):
                try:
                    if '.' in x:
                        x = float(x)
                    else:
                        x = int(x)
                except:
                    ...
            x = str(x)
            if not x and haveEmpty:
                haveEmpty[0] = True
            return x

    def _list_filter(self, l_s, white=True):
        """
        黑白名单过滤器.
        @param l_s: {参数:(参数值,..),..}
        @param white: 是不是白名单
        """
        if not l_s:
            return
        l_all = []  # [[参数,(参数值,..)],..], 加入没有的参数
        for i in self._paras_v:
            if i[0] in l_s:
                v = l_s[i[0]]
                assert isinstance(v, tuple), '参数值元组类型不是tuple!'
                assert len(set(v) & set(i[1])) == len(v), '名单参数值不在范围内!' + str(v) + ' not in ' + str(i[1])
                l_all.append([i[0], v])
            else:
                l_all.append(i)
        l_all_p = self._all_permutation(l_all)
        for i in l_all_p:
            self._all_p_v8m[i][1] = white

    @staticmethod
    def _all_permutation(paras, all=None, seq=None):
        """
        全排列算法.
        @param paras: [[参数,(参数值,..)],..]
        @return: [(排列参数),..]
        """
        if not paras:
            return []
        if seq is None:
            seq = []
        if all is None:
            all = []
        para_v_c = paras[0]
        for v in para_v_c[1]:
            if len(paras) <= 1:
                all.append(tuple(seq + [v]))
            else:
                ParaTex._all_permutation(paras[1:], all, seq + [v])
        return all

    def nextParas(self):
        """
        返回下一组要计算的参数.
        @return: {参数:参数值,..}, 若有ignoreP则返回部分参数
        """
        while True:
            self._index += 1
            if len(self._all_p) <= self._index:
                self._index = -1  # 重置
                self._alreadyP = set()
                return
            seq = self._all_p[self._index]
            seq_i = tuple([seq[i] for i, x in enumerate(self._paras_v) if x[0] not in self._ignoreP_s])
            if seq_i in self._alreadyP:
                continue
            if self._all_p_v8m[seq][1]:
                self._alreadyP.add(seq_i)
                paras_v = {x[0]: seq[i] for i, x in enumerate(self._paras_v) if x[0] not in self._ignoreP_s}
                yield paras_v

    def setParaV_c(self, paras_v: dict, c, setNoCompute=False):
        """
        根据一组参数设置对应的表内容, 内容符号需要注意, 用于latex.
        @param paras_v: {参数:参数值,..}, 允许多于表格参数
        @param c: other|list, 内容, 如果是列表说明有多个参数一起赋值, 按ignoreP参数全排列
        @param setNoCompute: bool, 是否设置为非计算, 即nextParas是否输出
        @return: dict, 插入成功的参数组数量, 插入重复的数量, 错误的数量,... 3者没有交集
        """
        seq = []  # 参数序列
        assert paras_v, 'paras_v 参数不能为空!'
        if isinstance(c, list) and len(c) == 1:
            c = c[0]
        out = {
            'success': 0,  # 成功不重复写入的参数组数量
            'repeat': 0,  # 和已有值重复的写入数量
            'error': 0,  # 无法写入的参数组数量
            'error_seq': [],  # 无法写入的参数组
        }
        paras_v = self._allToString(paras_v)
        c = self._allToString(c)
        if isinstance(c, list):
            ignoreP_num = reduce(operator.mul, [len(i[1]) for i in self._paras_v if i[0] not in paras_v], 1)  # 最小是1
            assert ignoreP_num == len(c), '忽律参数值数量与内容不匹配(%d!=%d)!' % (ignoreP_num, len(c))
            ignoreP = [(i, self._paras_v_D[i]) for i in self._ignoreP]  # [[参数,(参数值,..)],..], 没填的参数
            ignoreP_per = self._all_permutation(ignoreP)  # [(排列参数),..]
            for k, seq in enumerate(ignoreP_per):
                p_v = {ignoreP[i][0]: seq[i] for i in range(len(ignoreP))}
                p_v.update(paras_v)
                for i, j in self.setParaV_c(p_v, c[k], setNoCompute).items():
                    out[i] += j
        else:
            assert len(set(paras_v) & set(self._paras_v_D)) == len(self._paras_v), '参数数量不正确(%d!=%d)!' % (
                len(set(paras_v) | set(self._paras_v_D)), len(self._paras_v))
            for para, _ in self._paras_v:
                seq.append(paras_v[para])
            seq = tuple(seq)
            if seq in self._all_p_v8m:
                if setNoCompute:
                    self._all_p_v8m[seq][1] = False
                if self._all_p_v8m[seq][0] == c:
                    out['repeat'] += 1
                else:
                    self._all_p_v8m[seq][0] = c
                    out['success'] += 1
            else:
                out['error'] += 1
                out['error_seq'].append(seq)
        return out

    def getParasG_n(self, all=False):
        """
        获取一共有多少组参数.
        @param all: bool, 是不是全排列数量, 如果为False直接返回nextParas数量, 否则是全排列数量
        @return: int, 参数全排列有多少
        """
        allN = len(self._all_p)
        if not all:
            allN = 0
            for i in self.nextParas():
                allN += 1
        return allN

    def getParaVaddN(self, paraV: dict):
        """
        为参数和参数值获取参数名和参数值名, 若同一参数相同参数值一样则取第一个.
        @param paraV: {参数:参数值,..}
        @return: [(参数,参数名,参数值,参数值名),..]
        """
        out = []
        paraV = self._allToString(paraV)
        for i in self._leftParas + self._upParas:
            if i[0] not in paraV:
                continue
            k = j = None
            for k, j in enumerate(i[2]):
                if j == paraV[i[0]]:
                    break
            out.append((i[0], i[1], j, i[3][k]))
        return out

    def getTable(self, caption='Test', left_bf=False, up_bf=True, if_bf=max, dec=None, useV=False, path=None,
                 spMark='=' * 50, pathRepCheck=True):
        r"""
        输出表格, 需要latex包:
        \usepackage{multirow}  % 如果用到合并单元格
        \usepackage{CJKutf8}  % 如果包含中文
        @param caption: str, 标题
        @param left_bf: bool, 是否每行特殊值加粗
        @param up_bf: bool, 是否每列特殊值加粗
        @param if_bf: func, 是否加粗比较, 输入列表, 返回应该加粗的一个值. 一般是 max 或 min
        @param dec: None|int, 统一保留几位小数. 在加粗判断之后执行, 可能因为四舍五入导致看起来一样的值没有加粗
        @param useV: 是否使用参数和参数值作为表头(而不是参数名和参数值名)
        @param path: str, 保存路径, 追加模式写入
        @param spMark: str, 保存表格前输出的分割符号, 作为一行
        @param pathRepCheck: bool, 是否检查日志中已有一样的表格, 有则不输出, 这需要读取匹配全日志
        @return: str, latex表格
        """
        left_num = len(self._leftParas)  # 行参数数
        up_num = len(self._upParas)  # 列参数数
        left_numAll = reduce(operator.mul, [len(i[2]) for i in self._leftParas], 1)  # 总行数, 不含表头
        up_numAll = reduce(operator.mul, [len(i[2]) for i in self._upParas], 1)  # 总列数, 不含表头
        if len(self._upParas) == 1:
            up_numAll_1 = up_numAll
        else:
            up_numAll_1 = up_numAll // len(self._upParas[-1][2])  # 除最后一层 总列数
        cc = ('|' + 'c' * len(self._upParas[-1][2])) if len(self._upParas) > 1 else 'c'  # 合并列的表头
        assert left_numAll * up_numAll == len(self._all_p), '行列相乘不等于总数!'
        if useV:
            header1 = 0
            header2 = 2
        else:
            header1 = 1
            header2 = 3
        # 标题替换特殊字符
        caption = caption.replace('\\', r' ')
        caption = caption.replace('#', r'\#').replace('$', r'\$')
        caption = caption.replace('%', r'\%').replace('^', r'\^')
        caption = caption.replace('&', r'\&').replace('_', r'\_')
        caption = caption.replace('{', r'\{').replace('}', r'\}')
        # 头部
        table = '\\begin{table}[h]\n\\centering\n\\caption{%s}\n\\begin{tabular}{|%s} \\hline\n' % (
            caption, 'c|' * left_num + (cc * up_numAll_1).strip('|') + '|')
        # 表行头
        l = 1
        for i in range(up_num - 1):
            table += '\t'
            if left_num > 1:  # 需要占多行
                table += r'\multicolumn{%d}{|r|}{\bf{%s}}' % (left_num, str(self._upParas[i][header1]))
            else:  # 只有1列不需要占多行
                table += r'\bf{%s}' % str(self._upParas[i][header1])
            for k in range(l):  # 参数值名
                for j in self._upParas[i][header2]:
                    ll = up_numAll // len(self._upParas[i][3]) // l
                    if ll > 1:
                        x = r' & \multicolumn{%d}{|c|}{%s}' % (ll, str(j))
                    else:
                        x = ' & ' + str(j)
                    table += x
            if left_num > 1:
                table += r'\\ \cline{%d-%d}' % (left_num, left_num + up_numAll)
            else:
                table += r'\\ \hline'
            table += '\n'
            l *= len(self._upParas[i][3])
        # 表行头 最后一行
        table += '\t\\bf{%s}' % str(self._leftParas[0][header1])
        for i in range(1, left_num):
            if i == left_num - 1:
                table += r' & $_\textbf{%s}$' % str(self._leftParas[i][header1])
            else:
                table += r' & \bf{%s}' % str(self._leftParas[i][header1])
        table += r'\verb|\|$^\textbf{%s}$' % str(self._upParas[-1][header1])
        for i in range(l):
            for j in self._upParas[-1][header2]:
                table += ' & ' + str(j)
        table += '\\\\ \\hline \n'
        # 加粗
        all_v8bf_L = [[self._all_p_v8m[i][0], False] for i in self._all_p]  # [[值,是否加粗],..], 按 self._all_p 顺序

        def bf(y):  # 加粗函数, 返回对应索引
            try:
                x = [float('0' + str(i)) for i in y]
            except:
                x = [str(i) for i in y]
            xx = if_bf(x)
            return (lambda x: [j for j, i in enumerate(x) if i == xx])(x)

        if left_bf:
            for i in range(left_numAll):
                v_L = [i[0] for i in all_v8bf_L[i * up_numAll: (i + 1) * up_numAll]]
                for j in bf(v_L):
                    all_v8bf_L[j + i * up_numAll][1] = True
        if up_bf:
            for i in range(up_numAll):
                v_L = []
                x_L = []
                for j in range(left_numAll):
                    x = j * up_numAll + i
                    v_L.append(all_v8bf_L[x][0])
                    x_L.append(x)
                i_L = bf(v_L)
                for j in i_L:
                    all_v8bf_L[x_L[j]][1] = True
        # 内容
        cs_L = [''] * left_numAll  # 每一行值, 行表头s-内容-尾部

        def bf_v(i, j):  # 根据行列和加粗情况返回文本值
            v, b = all_v8bf_L[i * up_numAll + j]
            t = str(v).strip()
            if dec:  # 小数
                try:
                    t = ('%.' + str(dec) + 'f') % float(t)
                except:
                    ...
            if b and t:
                t = r'\bf{%s}' % t
            return t

        for i in range(left_numAll):  # 内容值
            cs_L[i] += bf_v(i, 0)
            for j in range(1, up_numAll):
                cs_L[i] += ' & ' + bf_v(i, j)
        default_s = '& '
        cs_L = [[default_s] * left_num + [i, r'\\'] for i in cs_L]  # 扩展多列
        l = left_numAll
        for j in range(left_num):  # 开头值
            l = l // len(self._leftParas[j][2])
            for i in range(left_numAll):
                if i % l == 0:  # l 步输出一个
                    ll = i // l % len(self._leftParas[j][2])  # 输出第几个值
                    if l > 1:
                        cs_L[i][j] = r'\multirow{%d}{*}{%s} ' % (l, self._leftParas[j][header2][ll]) + str(cs_L[i][j])
                    else:
                        cs_L[i][j] = r'%s ' % (str(self._leftParas[j][header2][ll])) + str(cs_L[i][j])
                    if i < left_numAll - 1 and j > 0:
                        for k in range(0, j):
                            if cs_L[i + 1][k] != default_s:
                                cs_L[i][-1] += r' \cline{%d-%d}' % (k + 1, left_num + up_numAll)
                                break
        cs_L[-1][-1] += r' \hline'
        for i in range(left_numAll):
            table += '\t' + ''.join(cs_L[i]) + '\n'
        # 尾部
        table += '\\end{tabular}\n\\end{table}'
        # 写入
        write = True
        if pathRepCheck and path and os.path.exists(path):
            with open(path, 'r', encoding='utf-8') as r:
                if table in r.read():
                    write = False
        if path and write:
            with open(path, 'a', encoding='utf-8') as w:
                w.write(spMark + '\n')
                w.write('time: ' + str(datetime.datetime.now()) + '\n')
                w.write('type: latex table\n')
                w.write(table + '\n')
        return table

    def getTableE(self, caption='Test', dec=None, useV=True, path=None, spMark='=' * 50, pathRepCheck=True):
        r"""
        输出 excel 表格, \t分割, 无加粗, 无合并单元格.
        @param caption: str, 标题
        @param dec: None|int, 统一保留几位小数
        @param useV: 是否使用参数和参数值作为表头(而不是参数名和参数值名), 只有 True 才能使用 readTableE
        @param path: str, 保存路径, 追加模式写入
        @param spMark: str, 保存表格前输出的分割符号, 作为一行
        @param pathRepCheck: bool, 是否检查日志中已有一样的表格, 有则不输出, 这需要读取匹配全日志
        @return: str, excel 表格
        """
        left_num = len(self._leftParas)  # 行参数数
        up_num = len(self._upParas)  # 列参数数
        left_numAll = reduce(operator.mul, [len(i[2]) for i in self._leftParas], 1)  # 总行数, 不含表头
        up_numAll = reduce(operator.mul, [len(i[2]) for i in self._upParas], 1)  # 总列数, 不含表头
        assert left_numAll * up_numAll == len(self._all_p), '行列相乘不等于总数!'
        if useV:
            header1 = 0
            header2 = 2
        else:
            header1 = 1
            header2 = 3
        # 头部
        table = caption + '\n'
        # 表行头
        l = 1
        for i in range(up_num - 1):
            table += '\t' * (left_num - 1)
            table += '%s' % str(self._upParas[i][header1])
            for k in range(l):  # 输出参数值名
                for j in self._upParas[i][header2]:
                    ll = up_numAll // len(self._upParas[i][3]) // l
                    if ll > 1:
                        x = '\t%s%s' % (str(j), '\t' * (ll - 1))
                    else:
                        x = '\t' + str(j)
                    table += x
            table += '\n'
            l *= len(self._upParas[i][3])
        # 表行头 最后一行
        table += '%s' % str(self._leftParas[0][header1])
        for i in range(1, left_num):
            table += '\t%s' % str(self._leftParas[i][header1])
        table += r'\%s' % str(self._upParas[-1][header1])
        for i in range(l):
            for j in self._upParas[-1][header2]:
                table += '\t' + str(j)
        # 内容
        cs_L = [''] * left_numAll  # 每一行, 行表头s-内容-尾部
        all_v_L = [self._all_p_v8m[i][0] for i in self._all_p]  # [值,..], 按 self._all_p 顺序

        def bf_v(i, j):  # 根据小数位数返回文本值
            v = all_v_L[i * up_numAll + j]
            t = str(v).strip()
            if dec:  # 小数
                try:
                    t = ('%.' + str(dec) + 'f') % float(t)
                except:
                    ...
            return t

        for i in range(left_numAll):  # 内容值
            cs_L[i] += bf_v(i, 0)
            for j in range(1, up_numAll):
                cs_L[i] += '\t' + bf_v(i, j)
        default_s = '\t'
        cs_L = [[default_s] * left_num + [i] for i in cs_L]  # 扩展多列
        l = left_numAll
        for j in range(left_num):  # 开头值
            l = l // len(self._leftParas[j][2])
            for i in range(left_numAll):
                if i % l == 0:  # l 步输出一个
                    ll = i // l % len(self._leftParas[j][2])  # 输出第几个值
                    cs_L[i][j] = r'%s ' % (str(self._leftParas[j][header2][ll])) + str(cs_L[i][j])
        for i in range(left_numAll):
            table += '\n' + ''.join(cs_L[i])
        # 写入
        write = True
        if pathRepCheck and path and os.path.exists(path):
            with open(path, 'r', encoding='utf-8') as r:
                if table in r.read():
                    write = False
        if path and write:
            with open(path, 'a', encoding='utf-8') as w:
                w.write(spMark + '\n')
                w.write('time: ' + str(datetime.datetime.now()) + '\n')
                w.write('type: excel table\n')
                w.write(table + '\n')
        return table

    def readTableE(self, path, setNoCompute=False, spMark='=' * 50, typeMark='type: excel table', lastOne=False,
                   simplifyOut=True):
        r'''
        用于将日志中 getTableE 输出的表格中的内容读取到表格中, 如果内容为空字符或None则不读取, 如果表格不规范可能导致读取程序报错或作为错误表格.
        读取的表格格式必须与 getTableE 输出到文件中的一致, 参数/参数名/参数值/参数值名都不可为空字符串和None, 不能包括\符号.
        getTableE 输出的必须是参数(值)(useV=True), 而不是参数值名(useV=False), 否则读取失败.
        末尾制表符不能少.
        @param path: str, 日志路径
        @param setNoCompute: bool, 日志中的值是否设置为非计算, 即nextParas是否输出
        @param spMark: str, 每组参数的上分隔符, 第一个分隔符上面的不看
        @param typeMark: str, 从 typeMark 开始下面第一行出现\t的地方开始读取表格, 到无\t行结束
        @param lastOne: bool, 是否只用日志中最后一个表格, False 表示日志中所有表格从上到下覆盖叠加, 如果为True前面的表格有效也不会检测
        @param simplifyOut: bool, 用于简化返回参数, 如果为True则不返回字符数超过100的统计参数
        @return: dict, 统计, 如果有的话 success+repeat = 不计算的参数组数量
        '''
        out = {
            'success': 0,  # 成功不重复写入的参数组数量
            'repeat': 0,  # 和已有值重复的写入数量
            'error_table': 0,  # 无效表格的数量
            'mark': 0,  # typeMark 的数量, 包含无效表格
        }
        try:
            with open(path, 'r', encoding='utf-8') as r:
                logs = r.read().split(spMark)[1:]
        except:
            return out
        tables = []  # [[[第一行第一格，..],..],..], 多个表格
        for k, log in enumerate(logs):  # 读取所有mask为表格的
            if typeMark not in log:
                continue
            out['mark'] += 1
            log = log.split(typeMark)[1].strip('\r\n').split('\n')
            start = False
            for line in log:
                if not start and '\t' in line:
                    start = True
                    tables.append([])  # [[第一行第一格，..],..]
                if start:
                    if '\t' in line:
                        tables[-1].append([i.strip() for i in line.split('\t')])  # [第一行第一格，..]
                    else:
                        break
        if lastOne:  # 只取最后一个
            tables = [tables[-1]]
        for ii, table in enumerate(tables):
            up_paras = []  # [参数,..], 上面参数(名)
            left_paras = []  # [参数,..], 左边参数(名)
            up_paras_V = []  # [[参数值,..],..], 上面参数值(名)
            left_paras_V = []  # [[参数值,..],..], 左边参数值(名)
            up_num = 0  # 上面参数种数
            left_num = 0  # 左边参数种数
            # 计算 left_num
            for i in table[0]:
                if not i:
                    left_num += 1
                else:
                    left_num += 1
                    break
            # 计算 up_num, up_paras
            for i in table:
                if '\\' not in i[left_num - 1]:
                    up_num += 1
                    up_paras.append(i[left_num - 1])
                else:
                    up_paras.append(i[left_num - 1].split('\\')[1])
                    up_num += 1
                    break
            # 计算 left_paras
            left_paras += table[up_num - 1][:left_num]
            left_paras[-1] = left_paras[-1].split('\\')[0]
            # 计算 up_paras_V
            next_num = len(table[0]) - left_num  # 下一个up参数的值数量
            for i in table[:up_num]:
                up_paras_V.append([])
                for j in i[left_num: left_num + next_num]:
                    if j:
                        next_num = 1
                        up_paras_V[-1].append(j)
                    else:
                        next_num += 1
            # 计算 left_paras_V
            next_num = len(table) - up_num  # 下一个left参数的值数量
            for i in range(left_num):
                left_paras_V.append([])
                for j in range(up_num, up_num + next_num):
                    k = table[j][i]
                    if k:
                        next_num = 1
                        left_paras_V[-1].append(k)
                    else:
                        next_num += 1
            # 构建全排列
            paras_v = [[left_paras[i], left_paras_V[i]] for i in range(left_num)]
            paras_v += [[up_paras[i], up_paras_V[i]] for i in range(up_num)]  # [[参数,(参数值,..)],..]
            error = False
            for i, j in paras_v:  # 查看表格参数是否错误
                if i not in self._paras_v_D or len(self._paras_v_D[i]) != len(j) or set(self._paras_v_D[i]) != set(j):
                    error = True
                    break
            if error or len(paras_v) != len(self._paras_v):
                out['error_table'] += 1
                continue
            all_p = self._all_permutation(paras_v)
            # 内容输入
            y = 0  # 第几个排列参数
            for i in range(up_num, len(table)):
                for j in range(left_num, len(table[0])):
                    x = {x[0]: all_p[y][i] for i, x in enumerate(paras_v)}
                    y += 1
                    try:
                        if not table[i][j] or table[i][j] == 'None':
                            continue
                    except:
                        raise ValueError('第%d个要读取的表中: table[%d][%d]不存在, 注意制表符和行数量!' % (ii + 1, i, j))
                    for k, v in self.setParaV_c(x, table[i][j], setNoCompute).items():
                        if k not in out:
                            out[k] = v
                        else:
                            out[k] += v
        if simplifyOut:
            out_ = {}
            for i, j in out.items():
                if len(str(j)) > 100:
                    continue
                else:
                    out_[i] = j
            out = out_
        return out

    def readParaLog(self, path, cv: list, spMark='=' * 50, paraMark='parameters: ', cMark='results: ',
                    setNoCompute=False, checkP=None, simplifyOut=True):
        r"""
        用于将日志中的内容读取到表格中, 日志例子:
        ...
        spMark\n
        paraMark{参数:参数值,..}\n
        cMark{内容名:内容值,..}\n
        ...
        @param path: 日志路径
        @param cv: str, 读取哪些内容名的值, 如果多个则顺序与ignoreP参数要求一致
        @param spMark: str, 每组参数的上分隔符, 第一个分隔符上面的不看
        @param paraMark: str, 参数字典的前缀标记, 必须顶行
        @param cMark: str, 内容字典的前缀标记, 必须顶行
        @param setNoCompute: bool, 日志中的值是否设置为非计算, 即nextParas是否输出
        @param checkP: {参数:参数值,..}, 用于检查日志中的其他参数是否一致
        @param simplifyOut: bool, 用于简化返回参数, 如果为True则不返回字符数超过100的统计参数
        @return: dict, 统计, 如果有的话success+repeat=非计算数量
        """
        if checkP is None:
            checkP = {}
        out = {
            'success': 0,  # 成功不重复写入的参数组数量
            'repeat': 0,  # 和已有值重复的写入数量
            'error': 0,  # 无法写入的参数组数量
            'error_seq': [],  # 无法写入的参数组
            'invalid': 0,  # 没有参数或内容的日志项数量
            'invalid_index': [],  # 没有参数或内容的日志项的索引, 从1开始
            'checkp_no_eq': 0,  # 检查额外参数不相等的参数组数量
        }
        checkP = self._allToString(checkP)
        try:
            with open(path, 'r', encoding='utf-8') as r:
                logs = r.read().split(spMark)[1:]
        except:
            return out
        for k, log in enumerate(logs):
            log = log.strip().split('\n')
            parasV, contentsV = {}, []
            for line in log:
                # line = line.strip()  # 不允许空格开头
                if line[:len(paraMark)] == paraMark:
                    parasV = ast.literal_eval(line.split(paraMark)[1])
                if line[:len(cMark)] == cMark:
                    contentsV = ast.literal_eval(line.split(cMark)[1])
                    contentsV = [contentsV[i] for i in cv]
            if parasV and contentsV:
                parasV = self._allToString(parasV)
                contentsV = self._allToString(contentsV)
                eq = True
                for i, j in checkP.items():
                    if i not in parasV or parasV[i] != j:
                        eq = False
                        break
                if eq:  # check 参数相等
                    for i, j in self.setParaV_c(parasV, contentsV, setNoCompute).items():
                        if i not in out:
                            out[i] = j
                        else:
                            out[i] += j
                else:  # 其他参数不相等
                    out['checkp_no_eq'] += 1
            else:
                out['invalid'] += 1
                out['invalid_index'].append(k + 1)
        if simplifyOut:
            out_ = {}
            for i, j in out.items():
                if len(str(j)) > 100:
                    continue
                else:
                    out_[i] = j
            out = out_
        return out


def paraTex_test():
    path = 'test/aa_result_test.log'
    # paraTex = ParaTex(
    #     leftParas=[['a', 'A', [1, 2], [10, 20]], ['b', 'B', [3, 8], [30, 80]]],
    #     upParas=[['c', 'C', [4], [40]], ['d', 'D', [5, 6, 7], [50, 60, 70]]],
    #     # blacklist=[{'a': (1,), 'c': (4,)}, {}],
    #     # whitelist=[{'a': (2,), 'c': (4,)}, {}],
    #     ignoreP=['b', 'd'],
    # )
    # print('paraTex._paras_v:', paraTex._paras_v)
    # print('paraTex._all_p:', paraTex._all_p)
    # print('paraTex._all_p_v8m:', paraTex._all_p_v8m)
    # for x in paraTex.nextParas():
    #     print(x)
    #     paraTex.setParaV_c(x, [1, 2, 3, 4, 5, 6])
    # print('paraTex._all_p_v8m:', paraTex._all_p_v8m)

    # paraTex = ParaTex(
    #     leftParas=[['a', 'A', [1, 2], [10, 20]], ['b', 'B', [3, 4], [30, 40]], ['f', 'F', [12, 13], [120, 130]]],
    #     upParas=[['c', 'C', [8, 9], [80, 90]], ['e', 'E', [10, 11], [100, 110]],
    #              ['d', 'D', [5, 6, 7], [50, 60, 70]]],
    #     # blacklist=[{'a': (1,), 'c': (4,)}, {}],
    #     # whitelist=[{'a': (2,), 'c': (4,)}, {}],
    # )
    # paraTex = ParaTex(
    #     leftParas=[['a', 'A', [1, 2], [10, 20]]],
    #     upParas=[['c', 'C', [4, 8, 9], [40, 80, 90]], ['b', 'B', [3, 4], [30, 40]]],
    #     # blacklist=[{'a': (1,), 'c': (4,)}, {}],
    #     # whitelist=[{'a': (2,), 'c': (4,)}, {}],
    # )
    # paraTex = ParaTex(
    #     leftParas=[['a', 'A', [1, 2], ['a1', 'a2']], ['b', 'B', [1, 2, 3], ['b1', 'b2', 'b3']],
    #                ['c', 'C', [1, 2, 3, 4, 5, 6], ['c1', 'c2', 'c3', 'c4', 'c5', 'c6']]],
    #     upParas=[['h', 'H', [1, 2], ['h1', 'h2']], ['i', 'I', [1, 2], ['i1', 'i2']],
    #              ['j', 'J', [1, 2], ['j1', 'j2']], ['k', 'K', [1, 2], ['k1', 'k2']]],
    # )
    # i = 0.001
    # n = 0
    # for x in paraTex.nextParas():
    #     x.update({12: 12})
    #     paraTex.setParaV_c(x, str(i))
    #     if n == 10:
    #         paraTex.setParaV_c(x, 3.1234)
    #     i += 0.001
    #     n += 1
    # # print('paraTex._leftParas:', paraTex._leftParas)
    # # print('paraTex._upParas:', paraTex._upParas)
    # print(paraTex.getTable(left_bf=False, up_bf=True, dec=4, if_bf=max, useV=False, path=path))
    # print(paraTex.getTableE(dec=4, useV=False, path=path))
    # print(paraTex.getParasG_n())
    paraTex = ParaTex(
        leftParas=[['h', 'H', [1, 2], ['h1', 'h2']], ['a', 'A', [1, 2], ['a1', 'a2']],
                   ['b', 'B', [1, 2, 3], ['b1', 'b2', 'b3']],
                   ['c', 'C', [1, 2, 3, 4, 5, 6], ['c1', 'c2', 'c3', 'c4', 'c5', 'c6']]],
        upParas=[['i', 'I', [1, 2], ['i1', 'i2']],
                 ['j', 'J', [1, 2], ['j1', 'j2']], ['k', 'K', [1, 2], ['k1', 'k2']]],
    )
    print(paraTex.readTableE(path, setNoCompute=True))
    print(paraTex.getTableE(dec=4, useV=False))
    print(paraTex.getParasG_n())


if __name__ == '__main__':
    paraTex_test()
