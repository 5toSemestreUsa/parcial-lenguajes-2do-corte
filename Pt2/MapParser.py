# Generated from Map.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,39,205,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        1,0,4,0,30,8,0,11,0,12,0,31,1,0,1,0,1,1,1,1,1,1,3,1,39,8,1,1,2,1,
        2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,3,2,55,8,2,1,3,
        1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,3,3,71,8,3,1,
        4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,3,4,83,8,4,1,5,1,5,1,5,1,5,
        1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,3,5,98,8,5,1,5,1,5,1,5,1,5,1,
        5,1,5,1,5,3,5,107,8,5,1,5,3,5,110,8,5,1,5,1,5,1,5,1,5,1,5,1,5,1,
        5,3,5,119,8,5,3,5,121,8,5,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,
        6,1,6,1,6,1,6,1,6,1,6,3,6,138,8,6,1,7,1,7,1,7,3,7,143,8,7,1,8,1,
        8,3,8,147,8,8,1,8,1,8,1,8,3,8,152,8,8,1,8,3,8,155,8,8,1,9,1,9,1,
        9,1,9,1,9,5,9,162,8,9,10,9,12,9,165,9,9,1,9,1,9,1,10,5,10,170,8,
        10,10,10,12,10,173,9,10,1,10,1,10,5,10,177,8,10,10,10,12,10,180,
        9,10,1,10,3,10,183,8,10,1,11,1,11,1,11,5,11,188,8,11,10,11,12,11,
        191,9,11,1,11,3,11,194,8,11,1,12,1,12,1,13,1,13,1,13,1,13,1,13,3,
        13,203,8,13,1,13,0,0,14,0,2,4,6,8,10,12,14,16,18,20,22,24,26,0,2,
        1,0,12,13,1,0,30,32,233,0,29,1,0,0,0,2,38,1,0,0,0,4,54,1,0,0,0,6,
        70,1,0,0,0,8,82,1,0,0,0,10,120,1,0,0,0,12,137,1,0,0,0,14,142,1,0,
        0,0,16,154,1,0,0,0,18,156,1,0,0,0,20,182,1,0,0,0,22,184,1,0,0,0,
        24,195,1,0,0,0,26,202,1,0,0,0,28,30,3,2,1,0,29,28,1,0,0,0,30,31,
        1,0,0,0,31,29,1,0,0,0,31,32,1,0,0,0,32,33,1,0,0,0,33,34,5,0,0,1,
        34,1,1,0,0,0,35,39,3,4,2,0,36,39,3,6,3,0,37,39,5,38,0,0,38,35,1,
        0,0,0,38,36,1,0,0,0,38,37,1,0,0,0,39,3,1,0,0,0,40,41,5,1,0,0,41,
        42,5,2,0,0,42,43,3,8,4,0,43,44,5,3,0,0,44,45,3,14,7,0,45,46,5,4,
        0,0,46,55,1,0,0,0,47,48,5,1,0,0,48,49,5,2,0,0,49,50,5,31,0,0,50,
        51,5,3,0,0,51,52,3,14,7,0,52,53,5,4,0,0,53,55,1,0,0,0,54,40,1,0,
        0,0,54,47,1,0,0,0,55,5,1,0,0,0,56,57,5,5,0,0,57,58,5,2,0,0,58,59,
        3,8,4,0,59,60,5,3,0,0,60,61,3,14,7,0,61,62,5,4,0,0,62,71,1,0,0,0,
        63,64,5,5,0,0,64,65,5,2,0,0,65,66,5,31,0,0,66,67,5,3,0,0,67,68,3,
        14,7,0,68,69,5,4,0,0,69,71,1,0,0,0,70,56,1,0,0,0,70,63,1,0,0,0,71,
        7,1,0,0,0,72,73,5,6,0,0,73,74,5,31,0,0,74,75,5,7,0,0,75,83,3,10,
        5,0,76,77,5,6,0,0,77,78,5,2,0,0,78,79,5,31,0,0,79,80,5,4,0,0,80,
        81,5,7,0,0,81,83,3,10,5,0,82,72,1,0,0,0,82,76,1,0,0,0,83,9,1,0,0,
        0,84,85,5,31,0,0,85,86,3,12,6,0,86,87,3,24,12,0,87,121,1,0,0,0,88,
        89,5,31,0,0,89,121,5,8,0,0,90,91,5,31,0,0,91,121,5,9,0,0,92,93,5,
        31,0,0,93,121,5,10,0,0,94,97,5,11,0,0,95,98,5,31,0,0,96,98,3,14,
        7,0,97,95,1,0,0,0,97,96,1,0,0,0,98,99,1,0,0,0,99,121,5,4,0,0,100,
        101,5,31,0,0,101,102,3,12,6,0,102,103,3,24,12,0,103,104,3,12,6,0,
        104,106,3,24,12,0,105,107,7,0,0,0,106,105,1,0,0,0,106,107,1,0,0,
        0,107,109,1,0,0,0,108,110,3,10,5,0,109,108,1,0,0,0,109,110,1,0,0,
        0,110,121,1,0,0,0,111,112,5,31,0,0,112,113,5,14,0,0,113,114,5,30,
        0,0,114,118,5,15,0,0,115,116,3,12,6,0,116,117,3,24,12,0,117,119,
        1,0,0,0,118,115,1,0,0,0,118,119,1,0,0,0,119,121,1,0,0,0,120,84,1,
        0,0,0,120,88,1,0,0,0,120,90,1,0,0,0,120,92,1,0,0,0,120,94,1,0,0,
        0,120,100,1,0,0,0,120,111,1,0,0,0,121,11,1,0,0,0,122,138,5,36,0,
        0,123,138,5,37,0,0,124,138,5,35,0,0,125,138,5,16,0,0,126,138,5,34,
        0,0,127,138,5,17,0,0,128,129,5,18,0,0,129,130,5,31,0,0,130,138,5,
        19,0,0,131,138,5,20,0,0,132,138,5,21,0,0,133,138,5,22,0,0,134,138,
        5,23,0,0,135,138,5,24,0,0,136,138,5,25,0,0,137,122,1,0,0,0,137,123,
        1,0,0,0,137,124,1,0,0,0,137,125,1,0,0,0,137,126,1,0,0,0,137,127,
        1,0,0,0,137,128,1,0,0,0,137,131,1,0,0,0,137,132,1,0,0,0,137,133,
        1,0,0,0,137,134,1,0,0,0,137,135,1,0,0,0,137,136,1,0,0,0,138,13,1,
        0,0,0,139,143,3,16,8,0,140,143,3,18,9,0,141,143,5,31,0,0,142,139,
        1,0,0,0,142,140,1,0,0,0,142,141,1,0,0,0,143,15,1,0,0,0,144,146,5,
        14,0,0,145,147,3,22,11,0,146,145,1,0,0,0,146,147,1,0,0,0,147,148,
        1,0,0,0,148,155,5,15,0,0,149,151,5,2,0,0,150,152,3,22,11,0,151,150,
        1,0,0,0,151,152,1,0,0,0,152,153,1,0,0,0,153,155,5,4,0,0,154,144,
        1,0,0,0,154,149,1,0,0,0,155,17,1,0,0,0,156,163,5,26,0,0,157,158,
        3,20,10,0,158,159,5,7,0,0,159,160,3,26,13,0,160,162,1,0,0,0,161,
        157,1,0,0,0,162,165,1,0,0,0,163,161,1,0,0,0,163,164,1,0,0,0,164,
        166,1,0,0,0,165,163,1,0,0,0,166,167,5,27,0,0,167,19,1,0,0,0,168,
        170,5,28,0,0,169,168,1,0,0,0,170,173,1,0,0,0,171,169,1,0,0,0,171,
        172,1,0,0,0,172,174,1,0,0,0,173,171,1,0,0,0,174,183,5,28,0,0,175,
        177,5,29,0,0,176,175,1,0,0,0,177,180,1,0,0,0,178,176,1,0,0,0,178,
        179,1,0,0,0,179,181,1,0,0,0,180,178,1,0,0,0,181,183,5,29,0,0,182,
        171,1,0,0,0,182,178,1,0,0,0,183,21,1,0,0,0,184,189,3,26,13,0,185,
        186,5,3,0,0,186,188,3,26,13,0,187,185,1,0,0,0,188,191,1,0,0,0,189,
        187,1,0,0,0,189,190,1,0,0,0,190,193,1,0,0,0,191,189,1,0,0,0,192,
        194,5,3,0,0,193,192,1,0,0,0,193,194,1,0,0,0,194,23,1,0,0,0,195,196,
        7,1,0,0,196,25,1,0,0,0,197,203,5,30,0,0,198,203,5,32,0,0,199,203,
        5,33,0,0,200,203,3,18,9,0,201,203,3,16,8,0,202,197,1,0,0,0,202,198,
        1,0,0,0,202,199,1,0,0,0,202,200,1,0,0,0,202,201,1,0,0,0,203,27,1,
        0,0,0,22,31,38,54,70,82,97,106,109,118,120,137,142,146,151,154,163,
        171,178,182,189,193,202
    ]

class MapParser ( Parser ):

    grammarFileName = "Map.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'map'", "'('", "','", "')'", "'filter'", 
                     "'lambda'", "':'", "'.upper()'", "'.lower()'", "'.capitalize()'", 
                     "'sorted('", "' and '", "' or '", "'['", "']'", "'%'", 
                     "'**'", "'.'", "'()'", "'=='", "'!='", "'<'", "'>'", 
                     "'<='", "'>='", "'{'", "'}'", "'\"'", "'''", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "'*'", "'/'", 
                     "'+'", "'-'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "INT", "ID", "FLOAT", "STRING", 
                      "MUL", "DIV", "ADD", "SUB", "NEWLINE", "WS" ]

    RULE_prog = 0
    RULE_stat = 1
    RULE_mapFunction = 2
    RULE_filterFunction = 3
    RULE_lambdaExpr = 4
    RULE_function = 5
    RULE_op = 6
    RULE_iterable = 7
    RULE_list = 8
    RULE_dict = 9
    RULE_key = 10
    RULE_elements = 11
    RULE_var = 12
    RULE_expr = 13

    ruleNames =  [ "prog", "stat", "mapFunction", "filterFunction", "lambdaExpr", 
                   "function", "op", "iterable", "list", "dict", "key", 
                   "elements", "var", "expr" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    T__16=17
    T__17=18
    T__18=19
    T__19=20
    T__20=21
    T__21=22
    T__22=23
    T__23=24
    T__24=25
    T__25=26
    T__26=27
    T__27=28
    T__28=29
    INT=30
    ID=31
    FLOAT=32
    STRING=33
    MUL=34
    DIV=35
    ADD=36
    SUB=37
    NEWLINE=38
    WS=39

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(MapParser.EOF, 0)

        def stat(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MapParser.StatContext)
            else:
                return self.getTypedRuleContext(MapParser.StatContext,i)


        def getRuleIndex(self):
            return MapParser.RULE_prog

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProg" ):
                listener.enterProg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProg" ):
                listener.exitProg(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProg" ):
                return visitor.visitProg(self)
            else:
                return visitor.visitChildren(self)




    def prog(self):

        localctx = MapParser.ProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_prog)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 29 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 28
                self.stat()
                self.state = 31 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 274877906978) != 0)):
                    break

            self.state = 33
            self.match(MapParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def mapFunction(self):
            return self.getTypedRuleContext(MapParser.MapFunctionContext,0)


        def filterFunction(self):
            return self.getTypedRuleContext(MapParser.FilterFunctionContext,0)


        def NEWLINE(self):
            return self.getToken(MapParser.NEWLINE, 0)

        def getRuleIndex(self):
            return MapParser.RULE_stat

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStat" ):
                listener.enterStat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStat" ):
                listener.exitStat(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStat" ):
                return visitor.visitStat(self)
            else:
                return visitor.visitChildren(self)




    def stat(self):

        localctx = MapParser.StatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_stat)
        try:
            self.state = 38
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 35
                self.mapFunction()
                pass
            elif token in [5]:
                self.enterOuterAlt(localctx, 2)
                self.state = 36
                self.filterFunction()
                pass
            elif token in [38]:
                self.enterOuterAlt(localctx, 3)
                self.state = 37
                self.match(MapParser.NEWLINE)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MapFunctionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def lambdaExpr(self):
            return self.getTypedRuleContext(MapParser.LambdaExprContext,0)


        def iterable(self):
            return self.getTypedRuleContext(MapParser.IterableContext,0)


        def ID(self):
            return self.getToken(MapParser.ID, 0)

        def getRuleIndex(self):
            return MapParser.RULE_mapFunction

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMapFunction" ):
                listener.enterMapFunction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMapFunction" ):
                listener.exitMapFunction(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMapFunction" ):
                return visitor.visitMapFunction(self)
            else:
                return visitor.visitChildren(self)




    def mapFunction(self):

        localctx = MapParser.MapFunctionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_mapFunction)
        try:
            self.state = 54
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 40
                self.match(MapParser.T__0)
                self.state = 41
                self.match(MapParser.T__1)
                self.state = 42
                self.lambdaExpr()
                self.state = 43
                self.match(MapParser.T__2)
                self.state = 44
                self.iterable()
                self.state = 45
                self.match(MapParser.T__3)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 47
                self.match(MapParser.T__0)
                self.state = 48
                self.match(MapParser.T__1)
                self.state = 49
                self.match(MapParser.ID)
                self.state = 50
                self.match(MapParser.T__2)
                self.state = 51
                self.iterable()
                self.state = 52
                self.match(MapParser.T__3)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FilterFunctionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def lambdaExpr(self):
            return self.getTypedRuleContext(MapParser.LambdaExprContext,0)


        def iterable(self):
            return self.getTypedRuleContext(MapParser.IterableContext,0)


        def ID(self):
            return self.getToken(MapParser.ID, 0)

        def getRuleIndex(self):
            return MapParser.RULE_filterFunction

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFilterFunction" ):
                listener.enterFilterFunction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFilterFunction" ):
                listener.exitFilterFunction(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFilterFunction" ):
                return visitor.visitFilterFunction(self)
            else:
                return visitor.visitChildren(self)




    def filterFunction(self):

        localctx = MapParser.FilterFunctionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_filterFunction)
        try:
            self.state = 70
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 56
                self.match(MapParser.T__4)
                self.state = 57
                self.match(MapParser.T__1)
                self.state = 58
                self.lambdaExpr()
                self.state = 59
                self.match(MapParser.T__2)
                self.state = 60
                self.iterable()
                self.state = 61
                self.match(MapParser.T__3)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 63
                self.match(MapParser.T__4)
                self.state = 64
                self.match(MapParser.T__1)
                self.state = 65
                self.match(MapParser.ID)
                self.state = 66
                self.match(MapParser.T__2)
                self.state = 67
                self.iterable()
                self.state = 68
                self.match(MapParser.T__3)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LambdaExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MapParser.ID, 0)

        def function(self):
            return self.getTypedRuleContext(MapParser.FunctionContext,0)


        def getRuleIndex(self):
            return MapParser.RULE_lambdaExpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLambdaExpr" ):
                listener.enterLambdaExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLambdaExpr" ):
                listener.exitLambdaExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLambdaExpr" ):
                return visitor.visitLambdaExpr(self)
            else:
                return visitor.visitChildren(self)




    def lambdaExpr(self):

        localctx = MapParser.LambdaExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_lambdaExpr)
        try:
            self.state = 82
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 72
                self.match(MapParser.T__5)
                self.state = 73
                self.match(MapParser.ID)
                self.state = 74
                self.match(MapParser.T__6)
                self.state = 75
                self.function()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 76
                self.match(MapParser.T__5)
                self.state = 77
                self.match(MapParser.T__1)
                self.state = 78
                self.match(MapParser.ID)
                self.state = 79
                self.match(MapParser.T__3)
                self.state = 80
                self.match(MapParser.T__6)
                self.state = 81
                self.function()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MapParser.ID, 0)

        def op(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MapParser.OpContext)
            else:
                return self.getTypedRuleContext(MapParser.OpContext,i)


        def var(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MapParser.VarContext)
            else:
                return self.getTypedRuleContext(MapParser.VarContext,i)


        def iterable(self):
            return self.getTypedRuleContext(MapParser.IterableContext,0)


        def function(self):
            return self.getTypedRuleContext(MapParser.FunctionContext,0)


        def INT(self):
            return self.getToken(MapParser.INT, 0)

        def getRuleIndex(self):
            return MapParser.RULE_function

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunction" ):
                listener.enterFunction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunction" ):
                listener.exitFunction(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunction" ):
                return visitor.visitFunction(self)
            else:
                return visitor.visitChildren(self)




    def function(self):

        localctx = MapParser.FunctionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_function)
        self._la = 0 # Token type
        try:
            self.state = 120
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 84
                self.match(MapParser.ID)
                self.state = 85
                self.op()
                self.state = 86
                self.var()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 88
                self.match(MapParser.ID)
                self.state = 89
                self.match(MapParser.T__7)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 90
                self.match(MapParser.ID)
                self.state = 91
                self.match(MapParser.T__8)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 92
                self.match(MapParser.ID)
                self.state = 93
                self.match(MapParser.T__9)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 94
                self.match(MapParser.T__10)
                self.state = 97
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
                if la_ == 1:
                    self.state = 95
                    self.match(MapParser.ID)
                    pass

                elif la_ == 2:
                    self.state = 96
                    self.iterable()
                    pass


                self.state = 99
                self.match(MapParser.T__3)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 100
                self.match(MapParser.ID)
                self.state = 101
                self.op()
                self.state = 102
                self.var()
                self.state = 103
                self.op()
                self.state = 104
                self.var()
                self.state = 106
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==12 or _la==13:
                    self.state = 105
                    _la = self._input.LA(1)
                    if not(_la==12 or _la==13):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()


                self.state = 109
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==11 or _la==31:
                    self.state = 108
                    self.function()


                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 111
                self.match(MapParser.ID)
                self.state = 112
                self.match(MapParser.T__13)
                self.state = 113
                self.match(MapParser.INT)
                self.state = 114
                self.match(MapParser.T__14)
                self.state = 118
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 257764556800) != 0):
                    self.state = 115
                    self.op()
                    self.state = 116
                    self.var()


                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ADD(self):
            return self.getToken(MapParser.ADD, 0)

        def SUB(self):
            return self.getToken(MapParser.SUB, 0)

        def DIV(self):
            return self.getToken(MapParser.DIV, 0)

        def MUL(self):
            return self.getToken(MapParser.MUL, 0)

        def ID(self):
            return self.getToken(MapParser.ID, 0)

        def getRuleIndex(self):
            return MapParser.RULE_op

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOp" ):
                listener.enterOp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOp" ):
                listener.exitOp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOp" ):
                return visitor.visitOp(self)
            else:
                return visitor.visitChildren(self)




    def op(self):

        localctx = MapParser.OpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_op)
        try:
            self.state = 137
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [36]:
                self.enterOuterAlt(localctx, 1)
                self.state = 122
                self.match(MapParser.ADD)
                pass
            elif token in [37]:
                self.enterOuterAlt(localctx, 2)
                self.state = 123
                self.match(MapParser.SUB)
                pass
            elif token in [35]:
                self.enterOuterAlt(localctx, 3)
                self.state = 124
                self.match(MapParser.DIV)
                pass
            elif token in [16]:
                self.enterOuterAlt(localctx, 4)
                self.state = 125
                self.match(MapParser.T__15)
                pass
            elif token in [34]:
                self.enterOuterAlt(localctx, 5)
                self.state = 126
                self.match(MapParser.MUL)
                pass
            elif token in [17]:
                self.enterOuterAlt(localctx, 6)
                self.state = 127
                self.match(MapParser.T__16)
                pass
            elif token in [18]:
                self.enterOuterAlt(localctx, 7)
                self.state = 128
                self.match(MapParser.T__17)
                self.state = 129
                self.match(MapParser.ID)
                self.state = 130
                self.match(MapParser.T__18)
                pass
            elif token in [20]:
                self.enterOuterAlt(localctx, 8)
                self.state = 131
                self.match(MapParser.T__19)
                pass
            elif token in [21]:
                self.enterOuterAlt(localctx, 9)
                self.state = 132
                self.match(MapParser.T__20)
                pass
            elif token in [22]:
                self.enterOuterAlt(localctx, 10)
                self.state = 133
                self.match(MapParser.T__21)
                pass
            elif token in [23]:
                self.enterOuterAlt(localctx, 11)
                self.state = 134
                self.match(MapParser.T__22)
                pass
            elif token in [24]:
                self.enterOuterAlt(localctx, 12)
                self.state = 135
                self.match(MapParser.T__23)
                pass
            elif token in [25]:
                self.enterOuterAlt(localctx, 13)
                self.state = 136
                self.match(MapParser.T__24)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IterableContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def list_(self):
            return self.getTypedRuleContext(MapParser.ListContext,0)


        def dict_(self):
            return self.getTypedRuleContext(MapParser.DictContext,0)


        def ID(self):
            return self.getToken(MapParser.ID, 0)

        def getRuleIndex(self):
            return MapParser.RULE_iterable

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIterable" ):
                listener.enterIterable(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIterable" ):
                listener.exitIterable(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIterable" ):
                return visitor.visitIterable(self)
            else:
                return visitor.visitChildren(self)




    def iterable(self):

        localctx = MapParser.IterableContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_iterable)
        try:
            self.state = 142
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [2, 14]:
                self.enterOuterAlt(localctx, 1)
                self.state = 139
                self.list_()
                pass
            elif token in [26]:
                self.enterOuterAlt(localctx, 2)
                self.state = 140
                self.dict_()
                pass
            elif token in [31]:
                self.enterOuterAlt(localctx, 3)
                self.state = 141
                self.match(MapParser.ID)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def elements(self):
            return self.getTypedRuleContext(MapParser.ElementsContext,0)


        def getRuleIndex(self):
            return MapParser.RULE_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterList" ):
                listener.enterList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitList" ):
                listener.exitList(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList" ):
                return visitor.visitList(self)
            else:
                return visitor.visitChildren(self)




    def list_(self):

        localctx = MapParser.ListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_list)
        self._la = 0 # Token type
        try:
            self.state = 154
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [14]:
                self.enterOuterAlt(localctx, 1)
                self.state = 144
                self.match(MapParser.T__13)
                self.state = 146
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 14025768964) != 0):
                    self.state = 145
                    self.elements()


                self.state = 148
                self.match(MapParser.T__14)
                pass
            elif token in [2]:
                self.enterOuterAlt(localctx, 2)
                self.state = 149
                self.match(MapParser.T__1)
                self.state = 151
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 14025768964) != 0):
                    self.state = 150
                    self.elements()


                self.state = 153
                self.match(MapParser.T__3)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DictContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def key(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MapParser.KeyContext)
            else:
                return self.getTypedRuleContext(MapParser.KeyContext,i)


        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MapParser.ExprContext)
            else:
                return self.getTypedRuleContext(MapParser.ExprContext,i)


        def getRuleIndex(self):
            return MapParser.RULE_dict

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDict" ):
                listener.enterDict(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDict" ):
                listener.exitDict(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDict" ):
                return visitor.visitDict(self)
            else:
                return visitor.visitChildren(self)




    def dict_(self):

        localctx = MapParser.DictContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_dict)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 156
            self.match(MapParser.T__25)
            self.state = 163
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==28 or _la==29:
                self.state = 157
                self.key()
                self.state = 158
                self.match(MapParser.T__6)
                self.state = 159
                self.expr()
                self.state = 165
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 166
            self.match(MapParser.T__26)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class KeyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MapParser.RULE_key

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterKey" ):
                listener.enterKey(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitKey" ):
                listener.exitKey(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitKey" ):
                return visitor.visitKey(self)
            else:
                return visitor.visitChildren(self)




    def key(self):

        localctx = MapParser.KeyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_key)
        try:
            self.state = 182
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [28]:
                self.enterOuterAlt(localctx, 1)
                self.state = 171
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,16,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 168
                        self.match(MapParser.T__27) 
                    self.state = 173
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,16,self._ctx)

                self.state = 174
                self.match(MapParser.T__27)
                pass
            elif token in [29]:
                self.enterOuterAlt(localctx, 2)
                self.state = 178
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,17,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 175
                        self.match(MapParser.T__28) 
                    self.state = 180
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,17,self._ctx)

                self.state = 181
                self.match(MapParser.T__28)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElementsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MapParser.ExprContext)
            else:
                return self.getTypedRuleContext(MapParser.ExprContext,i)


        def getRuleIndex(self):
            return MapParser.RULE_elements

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterElements" ):
                listener.enterElements(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitElements" ):
                listener.exitElements(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElements" ):
                return visitor.visitElements(self)
            else:
                return visitor.visitChildren(self)




    def elements(self):

        localctx = MapParser.ElementsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_elements)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 184
            self.expr()
            self.state = 189
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,19,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 185
                    self.match(MapParser.T__2)
                    self.state = 186
                    self.expr() 
                self.state = 191
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,19,self._ctx)

            self.state = 193
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==3:
                self.state = 192
                self.match(MapParser.T__2)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VarContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MapParser.ID, 0)

        def INT(self):
            return self.getToken(MapParser.INT, 0)

        def FLOAT(self):
            return self.getToken(MapParser.FLOAT, 0)

        def getRuleIndex(self):
            return MapParser.RULE_var

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVar" ):
                listener.enterVar(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVar" ):
                listener.exitVar(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar" ):
                return visitor.visitVar(self)
            else:
                return visitor.visitChildren(self)




    def var(self):

        localctx = MapParser.VarContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_var)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 195
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 7516192768) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(MapParser.INT, 0)

        def FLOAT(self):
            return self.getToken(MapParser.FLOAT, 0)

        def STRING(self):
            return self.getToken(MapParser.STRING, 0)

        def dict_(self):
            return self.getTypedRuleContext(MapParser.DictContext,0)


        def list_(self):
            return self.getTypedRuleContext(MapParser.ListContext,0)


        def getRuleIndex(self):
            return MapParser.RULE_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr" ):
                listener.enterExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr" ):
                listener.exitExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)




    def expr(self):

        localctx = MapParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_expr)
        try:
            self.state = 202
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [30]:
                self.enterOuterAlt(localctx, 1)
                self.state = 197
                self.match(MapParser.INT)
                pass
            elif token in [32]:
                self.enterOuterAlt(localctx, 2)
                self.state = 198
                self.match(MapParser.FLOAT)
                pass
            elif token in [33]:
                self.enterOuterAlt(localctx, 3)
                self.state = 199
                self.match(MapParser.STRING)
                pass
            elif token in [26]:
                self.enterOuterAlt(localctx, 4)
                self.state = 200
                self.dict_()
                pass
            elif token in [2, 14]:
                self.enterOuterAlt(localctx, 5)
                self.state = 201
                self.list_()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





