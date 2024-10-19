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
        4,1,31,228,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,1,0,4,0,32,8,0,11,0,12,0,33,1,0,1,0,1,1,1,1,1,1,3,1,41,
        8,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,3,2,
        57,8,2,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,3,
        3,73,8,3,1,4,1,4,1,4,1,4,1,4,3,4,80,8,4,1,5,1,5,1,5,1,5,1,5,1,5,
        1,5,1,5,1,5,1,5,5,5,92,8,5,10,5,12,5,95,9,5,1,5,1,5,1,5,1,5,1,5,
        1,5,1,5,1,5,3,5,105,8,5,3,5,107,8,5,1,6,1,6,1,6,1,6,1,6,1,6,4,6,
        115,8,6,11,6,12,6,116,1,6,3,6,120,8,6,1,6,1,6,1,6,1,6,1,6,3,6,127,
        8,6,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,
        1,7,1,7,3,7,146,8,7,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,5,8,156,8,8,
        10,8,12,8,159,9,8,1,8,3,8,162,8,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,
        8,3,8,172,8,8,1,9,1,9,3,9,176,8,9,1,9,1,9,1,9,3,9,181,8,9,1,9,3,
        9,184,8,9,1,10,1,10,1,10,1,10,1,10,5,10,191,8,10,10,10,12,10,194,
        9,10,1,10,1,10,1,11,1,11,5,11,200,8,11,10,11,12,11,203,9,11,1,11,
        1,11,1,12,1,12,1,13,1,13,1,13,5,13,212,8,13,10,13,12,13,215,9,13,
        1,13,3,13,218,8,13,1,14,1,14,1,14,1,14,1,14,1,14,3,14,226,8,14,1,
        14,0,0,15,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,0,0,260,0,31,1,
        0,0,0,2,40,1,0,0,0,4,56,1,0,0,0,6,72,1,0,0,0,8,79,1,0,0,0,10,106,
        1,0,0,0,12,126,1,0,0,0,14,145,1,0,0,0,16,171,1,0,0,0,18,183,1,0,
        0,0,20,185,1,0,0,0,22,197,1,0,0,0,24,206,1,0,0,0,26,208,1,0,0,0,
        28,225,1,0,0,0,30,32,3,2,1,0,31,30,1,0,0,0,32,33,1,0,0,0,33,31,1,
        0,0,0,33,34,1,0,0,0,34,35,1,0,0,0,35,36,5,0,0,1,36,1,1,0,0,0,37,
        41,3,4,2,0,38,41,3,6,3,0,39,41,5,30,0,0,40,37,1,0,0,0,40,38,1,0,
        0,0,40,39,1,0,0,0,41,3,1,0,0,0,42,43,5,1,0,0,43,44,5,2,0,0,44,45,
        3,8,4,0,45,46,5,3,0,0,46,47,3,16,8,0,47,48,5,4,0,0,48,57,1,0,0,0,
        49,50,5,1,0,0,50,51,5,2,0,0,51,52,3,10,5,0,52,53,5,3,0,0,53,54,3,
        16,8,0,54,55,5,4,0,0,55,57,1,0,0,0,56,42,1,0,0,0,56,49,1,0,0,0,57,
        5,1,0,0,0,58,59,5,5,0,0,59,60,5,2,0,0,60,61,3,8,4,0,61,62,5,3,0,
        0,62,63,3,16,8,0,63,64,5,4,0,0,64,73,1,0,0,0,65,66,5,5,0,0,66,67,
        5,2,0,0,67,68,3,10,5,0,68,69,5,3,0,0,69,70,3,16,8,0,70,71,5,4,0,
        0,71,73,1,0,0,0,72,58,1,0,0,0,72,65,1,0,0,0,73,7,1,0,0,0,74,80,1,
        0,0,0,75,76,5,6,0,0,76,77,5,23,0,0,77,78,5,7,0,0,78,80,3,10,5,0,
        79,74,1,0,0,0,79,75,1,0,0,0,80,9,1,0,0,0,81,107,3,28,14,0,82,83,
        3,28,14,0,83,84,3,14,7,0,84,107,1,0,0,0,85,86,3,28,14,0,86,87,3,
        14,7,0,87,93,3,28,14,0,88,89,3,14,7,0,89,90,3,28,14,0,90,92,1,0,
        0,0,91,88,1,0,0,0,92,95,1,0,0,0,93,91,1,0,0,0,93,94,1,0,0,0,94,107,
        1,0,0,0,95,93,1,0,0,0,96,107,3,12,6,0,97,98,3,28,14,0,98,99,5,8,
        0,0,99,100,3,28,14,0,100,104,5,9,0,0,101,102,3,14,7,0,102,103,3,
        8,4,0,103,105,1,0,0,0,104,101,1,0,0,0,104,105,1,0,0,0,105,107,1,
        0,0,0,106,81,1,0,0,0,106,82,1,0,0,0,106,85,1,0,0,0,106,96,1,0,0,
        0,106,97,1,0,0,0,107,11,1,0,0,0,108,127,1,0,0,0,109,110,5,23,0,0,
        110,111,5,2,0,0,111,114,3,28,14,0,112,113,5,3,0,0,113,115,3,28,14,
        0,114,112,1,0,0,0,115,116,1,0,0,0,116,114,1,0,0,0,116,117,1,0,0,
        0,117,119,1,0,0,0,118,120,5,3,0,0,119,118,1,0,0,0,119,120,1,0,0,
        0,120,121,1,0,0,0,121,122,5,4,0,0,122,127,1,0,0,0,123,124,5,23,0,
        0,124,125,5,2,0,0,125,127,5,4,0,0,126,108,1,0,0,0,126,109,1,0,0,
        0,126,123,1,0,0,0,127,13,1,0,0,0,128,146,5,28,0,0,129,146,5,29,0,
        0,130,146,5,27,0,0,131,146,5,10,0,0,132,146,5,26,0,0,133,146,5,11,
        0,0,134,135,5,12,0,0,135,136,5,23,0,0,136,146,5,13,0,0,137,138,5,
        12,0,0,138,146,5,23,0,0,139,146,5,14,0,0,140,146,5,15,0,0,141,146,
        5,16,0,0,142,146,5,17,0,0,143,146,5,18,0,0,144,146,5,19,0,0,145,
        128,1,0,0,0,145,129,1,0,0,0,145,130,1,0,0,0,145,131,1,0,0,0,145,
        132,1,0,0,0,145,133,1,0,0,0,145,134,1,0,0,0,145,137,1,0,0,0,145,
        139,1,0,0,0,145,140,1,0,0,0,145,141,1,0,0,0,145,142,1,0,0,0,145,
        143,1,0,0,0,145,144,1,0,0,0,146,15,1,0,0,0,147,172,3,18,9,0,148,
        172,3,20,10,0,149,172,3,22,11,0,150,151,5,23,0,0,151,152,5,2,0,0,
        152,157,3,28,14,0,153,154,5,3,0,0,154,156,3,28,14,0,155,153,1,0,
        0,0,156,159,1,0,0,0,157,155,1,0,0,0,157,158,1,0,0,0,158,161,1,0,
        0,0,159,157,1,0,0,0,160,162,5,3,0,0,161,160,1,0,0,0,161,162,1,0,
        0,0,162,163,1,0,0,0,163,164,5,4,0,0,164,172,1,0,0,0,165,166,5,23,
        0,0,166,167,5,2,0,0,167,168,3,28,14,0,168,169,5,4,0,0,169,172,1,
        0,0,0,170,172,5,23,0,0,171,147,1,0,0,0,171,148,1,0,0,0,171,149,1,
        0,0,0,171,150,1,0,0,0,171,165,1,0,0,0,171,170,1,0,0,0,172,17,1,0,
        0,0,173,175,5,8,0,0,174,176,3,26,13,0,175,174,1,0,0,0,175,176,1,
        0,0,0,176,177,1,0,0,0,177,184,5,9,0,0,178,180,5,2,0,0,179,181,3,
        26,13,0,180,179,1,0,0,0,180,181,1,0,0,0,181,182,1,0,0,0,182,184,
        5,4,0,0,183,173,1,0,0,0,183,178,1,0,0,0,184,19,1,0,0,0,185,192,5,
        20,0,0,186,187,3,24,12,0,187,188,5,7,0,0,188,189,3,28,14,0,189,191,
        1,0,0,0,190,186,1,0,0,0,191,194,1,0,0,0,192,190,1,0,0,0,192,193,
        1,0,0,0,193,195,1,0,0,0,194,192,1,0,0,0,195,196,5,21,0,0,196,21,
        1,0,0,0,197,201,5,20,0,0,198,200,3,26,13,0,199,198,1,0,0,0,200,203,
        1,0,0,0,201,199,1,0,0,0,201,202,1,0,0,0,202,204,1,0,0,0,203,201,
        1,0,0,0,204,205,5,21,0,0,205,23,1,0,0,0,206,207,5,25,0,0,207,25,
        1,0,0,0,208,213,3,28,14,0,209,210,5,3,0,0,210,212,3,28,14,0,211,
        209,1,0,0,0,212,215,1,0,0,0,213,211,1,0,0,0,213,214,1,0,0,0,214,
        217,1,0,0,0,215,213,1,0,0,0,216,218,5,3,0,0,217,216,1,0,0,0,217,
        218,1,0,0,0,218,27,1,0,0,0,219,226,5,22,0,0,220,226,5,24,0,0,221,
        226,5,25,0,0,222,226,3,20,10,0,223,226,3,18,9,0,224,226,5,23,0,0,
        225,219,1,0,0,0,225,220,1,0,0,0,225,221,1,0,0,0,225,222,1,0,0,0,
        225,223,1,0,0,0,225,224,1,0,0,0,226,29,1,0,0,0,23,33,40,56,72,79,
        93,104,106,116,119,126,145,157,161,171,175,180,183,192,201,213,217,
        225
    ]

class MapParser ( Parser ):

    grammarFileName = "Map.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'map'", "'('", "','", "')'", "'filter'", 
                     "'lambda'", "':'", "'['", "']'", "'%'", "'**'", "'.'", 
                     "'()'", "'=='", "'!='", "'<'", "'>'", "'<='", "'>='", 
                     "'{'", "'}'", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "'*'", "'/'", "'+'", "'-'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
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
    RULE_functionCall = 6
    RULE_op = 7
    RULE_iterable = 8
    RULE_list = 9
    RULE_dict = 10
    RULE_set = 11
    RULE_key = 12
    RULE_elements = 13
    RULE_expr = 14

    ruleNames =  [ "prog", "stat", "mapFunction", "filterFunction", "lambdaExpr", 
                   "function", "functionCall", "op", "iterable", "list", 
                   "dict", "set", "key", "elements", "expr" ]

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
    INT=22
    ID=23
    FLOAT=24
    STRING=25
    MUL=26
    DIV=27
    ADD=28
    SUB=29
    NEWLINE=30
    WS=31

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
            self.state = 31 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 30
                self.stat()
                self.state = 33 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 1073741858) != 0)):
                    break

            self.state = 35
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
            self.state = 40
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 37
                self.mapFunction()
                pass
            elif token in [5]:
                self.enterOuterAlt(localctx, 2)
                self.state = 38
                self.filterFunction()
                pass
            elif token in [30]:
                self.enterOuterAlt(localctx, 3)
                self.state = 39
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


        def function(self):
            return self.getTypedRuleContext(MapParser.FunctionContext,0)


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
            self.state = 56
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 42
                self.match(MapParser.T__0)
                self.state = 43
                self.match(MapParser.T__1)
                self.state = 44
                self.lambdaExpr()
                self.state = 45
                self.match(MapParser.T__2)
                self.state = 46
                self.iterable()
                self.state = 47
                self.match(MapParser.T__3)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 49
                self.match(MapParser.T__0)
                self.state = 50
                self.match(MapParser.T__1)
                self.state = 51
                self.function()
                self.state = 52
                self.match(MapParser.T__2)
                self.state = 53
                self.iterable()
                self.state = 54
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


        def function(self):
            return self.getTypedRuleContext(MapParser.FunctionContext,0)


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
            self.state = 72
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 58
                self.match(MapParser.T__4)
                self.state = 59
                self.match(MapParser.T__1)
                self.state = 60
                self.lambdaExpr()
                self.state = 61
                self.match(MapParser.T__2)
                self.state = 62
                self.iterable()
                self.state = 63
                self.match(MapParser.T__3)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 65
                self.match(MapParser.T__4)
                self.state = 66
                self.match(MapParser.T__1)
                self.state = 67
                self.function()
                self.state = 68
                self.match(MapParser.T__2)
                self.state = 69
                self.iterable()
                self.state = 70
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
            self.state = 79
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [3]:
                self.enterOuterAlt(localctx, 1)

                pass
            elif token in [6]:
                self.enterOuterAlt(localctx, 2)
                self.state = 75
                self.match(MapParser.T__5)
                self.state = 76
                self.match(MapParser.ID)
                self.state = 77
                self.match(MapParser.T__6)
                self.state = 78
                self.function()
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


    class FunctionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MapParser.ExprContext)
            else:
                return self.getTypedRuleContext(MapParser.ExprContext,i)


        def op(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MapParser.OpContext)
            else:
                return self.getTypedRuleContext(MapParser.OpContext,i)


        def functionCall(self):
            return self.getTypedRuleContext(MapParser.FunctionCallContext,0)


        def lambdaExpr(self):
            return self.getTypedRuleContext(MapParser.LambdaExprContext,0)


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
            self.state = 106
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 81
                self.expr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 82
                self.expr()
                self.state = 83
                self.op()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 85
                self.expr()
                self.state = 86
                self.op()
                self.state = 87
                self.expr()
                self.state = 93
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1007672320) != 0):
                    self.state = 88
                    self.op()
                    self.state = 89
                    self.expr()
                    self.state = 95
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 96
                self.functionCall()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 97
                self.expr()
                self.state = 98
                self.match(MapParser.T__7)
                self.state = 99
                self.expr()
                self.state = 100
                self.match(MapParser.T__8)
                self.state = 104
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 1007672320) != 0):
                    self.state = 101
                    self.op()
                    self.state = 102
                    self.lambdaExpr()


                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionCallContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MapParser.ID, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MapParser.ExprContext)
            else:
                return self.getTypedRuleContext(MapParser.ExprContext,i)


        def getRuleIndex(self):
            return MapParser.RULE_functionCall

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctionCall" ):
                listener.enterFunctionCall(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctionCall" ):
                listener.exitFunctionCall(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunctionCall" ):
                return visitor.visitFunctionCall(self)
            else:
                return visitor.visitChildren(self)




    def functionCall(self):

        localctx = MapParser.FunctionCallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_functionCall)
        self._la = 0 # Token type
        try:
            self.state = 126
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 109
                self.match(MapParser.ID)
                self.state = 110
                self.match(MapParser.T__1)
                self.state = 111
                self.expr()
                self.state = 114 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 112
                        self.match(MapParser.T__2)
                        self.state = 113
                        self.expr()

                    else:
                        raise NoViableAltException(self)
                    self.state = 116 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,8,self._ctx)

                self.state = 119
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==3:
                    self.state = 118
                    self.match(MapParser.T__2)


                self.state = 121
                self.match(MapParser.T__3)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 123
                self.match(MapParser.ID)
                self.state = 124
                self.match(MapParser.T__1)
                self.state = 125
                self.match(MapParser.T__3)
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
        self.enterRule(localctx, 14, self.RULE_op)
        try:
            self.state = 145
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 128
                self.match(MapParser.ADD)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 129
                self.match(MapParser.SUB)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 130
                self.match(MapParser.DIV)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 131
                self.match(MapParser.T__9)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 132
                self.match(MapParser.MUL)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 133
                self.match(MapParser.T__10)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 134
                self.match(MapParser.T__11)
                self.state = 135
                self.match(MapParser.ID)
                self.state = 136
                self.match(MapParser.T__12)
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 137
                self.match(MapParser.T__11)
                self.state = 138
                self.match(MapParser.ID)
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 139
                self.match(MapParser.T__13)
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 140
                self.match(MapParser.T__14)
                pass

            elif la_ == 11:
                self.enterOuterAlt(localctx, 11)
                self.state = 141
                self.match(MapParser.T__15)
                pass

            elif la_ == 12:
                self.enterOuterAlt(localctx, 12)
                self.state = 142
                self.match(MapParser.T__16)
                pass

            elif la_ == 13:
                self.enterOuterAlt(localctx, 13)
                self.state = 143
                self.match(MapParser.T__17)
                pass

            elif la_ == 14:
                self.enterOuterAlt(localctx, 14)
                self.state = 144
                self.match(MapParser.T__18)
                pass


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


        def set_(self):
            return self.getTypedRuleContext(MapParser.SetContext,0)


        def ID(self):
            return self.getToken(MapParser.ID, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MapParser.ExprContext)
            else:
                return self.getTypedRuleContext(MapParser.ExprContext,i)


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
        self.enterRule(localctx, 16, self.RULE_iterable)
        self._la = 0 # Token type
        try:
            self.state = 171
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 147
                self.list_()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 148
                self.dict_()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 149
                self.set_()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 150
                self.match(MapParser.ID)
                self.state = 151
                self.match(MapParser.T__1)
                self.state = 152
                self.expr()
                self.state = 157
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,12,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 153
                        self.match(MapParser.T__2)
                        self.state = 154
                        self.expr() 
                    self.state = 159
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,12,self._ctx)

                self.state = 161
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==3:
                    self.state = 160
                    self.match(MapParser.T__2)


                self.state = 163
                self.match(MapParser.T__3)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 165
                self.match(MapParser.ID)
                self.state = 166
                self.match(MapParser.T__1)
                self.state = 167
                self.expr()
                self.state = 168
                self.match(MapParser.T__3)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 170
                self.match(MapParser.ID)
                pass


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
        self.enterRule(localctx, 18, self.RULE_list)
        self._la = 0 # Token type
        try:
            self.state = 183
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [8]:
                self.enterOuterAlt(localctx, 1)
                self.state = 173
                self.match(MapParser.T__7)
                self.state = 175
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 63963396) != 0):
                    self.state = 174
                    self.elements()


                self.state = 177
                self.match(MapParser.T__8)
                pass
            elif token in [2]:
                self.enterOuterAlt(localctx, 2)
                self.state = 178
                self.match(MapParser.T__1)
                self.state = 180
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 63963396) != 0):
                    self.state = 179
                    self.elements()


                self.state = 182
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
        self.enterRule(localctx, 20, self.RULE_dict)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 185
            self.match(MapParser.T__19)
            self.state = 192
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==25:
                self.state = 186
                self.key()
                self.state = 187
                self.match(MapParser.T__6)
                self.state = 188
                self.expr()
                self.state = 194
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 195
            self.match(MapParser.T__20)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SetContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def elements(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MapParser.ElementsContext)
            else:
                return self.getTypedRuleContext(MapParser.ElementsContext,i)


        def getRuleIndex(self):
            return MapParser.RULE_set

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSet" ):
                listener.enterSet(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSet" ):
                listener.exitSet(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSet" ):
                return visitor.visitSet(self)
            else:
                return visitor.visitChildren(self)




    def set_(self):

        localctx = MapParser.SetContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_set)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 197
            self.match(MapParser.T__19)
            self.state = 201
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 63963396) != 0):
                self.state = 198
                self.elements()
                self.state = 203
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 204
            self.match(MapParser.T__20)
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

        def STRING(self):
            return self.getToken(MapParser.STRING, 0)

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
        self.enterRule(localctx, 24, self.RULE_key)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 206
            self.match(MapParser.STRING)
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
        self.enterRule(localctx, 26, self.RULE_elements)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 208
            self.expr()
            self.state = 213
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,20,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 209
                    self.match(MapParser.T__2)
                    self.state = 210
                    self.expr() 
                self.state = 215
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,20,self._ctx)

            self.state = 217
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==3:
                self.state = 216
                self.match(MapParser.T__2)


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


        def ID(self):
            return self.getToken(MapParser.ID, 0)

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
        self.enterRule(localctx, 28, self.RULE_expr)
        try:
            self.state = 225
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [22]:
                self.enterOuterAlt(localctx, 1)
                self.state = 219
                self.match(MapParser.INT)
                pass
            elif token in [24]:
                self.enterOuterAlt(localctx, 2)
                self.state = 220
                self.match(MapParser.FLOAT)
                pass
            elif token in [25]:
                self.enterOuterAlt(localctx, 3)
                self.state = 221
                self.match(MapParser.STRING)
                pass
            elif token in [20]:
                self.enterOuterAlt(localctx, 4)
                self.state = 222
                self.dict_()
                pass
            elif token in [2, 8]:
                self.enterOuterAlt(localctx, 5)
                self.state = 223
                self.list_()
                pass
            elif token in [23]:
                self.enterOuterAlt(localctx, 6)
                self.state = 224
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





