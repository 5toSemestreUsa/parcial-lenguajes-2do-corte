# Generated from Map.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .MapParser import MapParser
else:
    from MapParser import MapParser

# This class defines a complete listener for a parse tree produced by MapParser.
class MapListener(ParseTreeListener):

    # Enter a parse tree produced by MapParser#prog.
    def enterProg(self, ctx:MapParser.ProgContext):
        pass

    # Exit a parse tree produced by MapParser#prog.
    def exitProg(self, ctx:MapParser.ProgContext):
        pass


    # Enter a parse tree produced by MapParser#stat.
    def enterStat(self, ctx:MapParser.StatContext):
        pass

    # Exit a parse tree produced by MapParser#stat.
    def exitStat(self, ctx:MapParser.StatContext):
        pass


    # Enter a parse tree produced by MapParser#mapFunction.
    def enterMapFunction(self, ctx:MapParser.MapFunctionContext):
        pass

    # Exit a parse tree produced by MapParser#mapFunction.
    def exitMapFunction(self, ctx:MapParser.MapFunctionContext):
        pass


    # Enter a parse tree produced by MapParser#filterFunction.
    def enterFilterFunction(self, ctx:MapParser.FilterFunctionContext):
        pass

    # Exit a parse tree produced by MapParser#filterFunction.
    def exitFilterFunction(self, ctx:MapParser.FilterFunctionContext):
        pass


    # Enter a parse tree produced by MapParser#lambdaExpr.
    def enterLambdaExpr(self, ctx:MapParser.LambdaExprContext):
        pass

    # Exit a parse tree produced by MapParser#lambdaExpr.
    def exitLambdaExpr(self, ctx:MapParser.LambdaExprContext):
        pass


    # Enter a parse tree produced by MapParser#function.
    def enterFunction(self, ctx:MapParser.FunctionContext):
        pass

    # Exit a parse tree produced by MapParser#function.
    def exitFunction(self, ctx:MapParser.FunctionContext):
        pass


    # Enter a parse tree produced by MapParser#functionCall.
    def enterFunctionCall(self, ctx:MapParser.FunctionCallContext):
        pass

    # Exit a parse tree produced by MapParser#functionCall.
    def exitFunctionCall(self, ctx:MapParser.FunctionCallContext):
        pass


    # Enter a parse tree produced by MapParser#op.
    def enterOp(self, ctx:MapParser.OpContext):
        pass

    # Exit a parse tree produced by MapParser#op.
    def exitOp(self, ctx:MapParser.OpContext):
        pass


    # Enter a parse tree produced by MapParser#iterable.
    def enterIterable(self, ctx:MapParser.IterableContext):
        pass

    # Exit a parse tree produced by MapParser#iterable.
    def exitIterable(self, ctx:MapParser.IterableContext):
        pass


    # Enter a parse tree produced by MapParser#list.
    def enterList(self, ctx:MapParser.ListContext):
        pass

    # Exit a parse tree produced by MapParser#list.
    def exitList(self, ctx:MapParser.ListContext):
        pass


    # Enter a parse tree produced by MapParser#dict.
    def enterDict(self, ctx:MapParser.DictContext):
        pass

    # Exit a parse tree produced by MapParser#dict.
    def exitDict(self, ctx:MapParser.DictContext):
        pass


    # Enter a parse tree produced by MapParser#set.
    def enterSet(self, ctx:MapParser.SetContext):
        pass

    # Exit a parse tree produced by MapParser#set.
    def exitSet(self, ctx:MapParser.SetContext):
        pass


    # Enter a parse tree produced by MapParser#key.
    def enterKey(self, ctx:MapParser.KeyContext):
        pass

    # Exit a parse tree produced by MapParser#key.
    def exitKey(self, ctx:MapParser.KeyContext):
        pass


    # Enter a parse tree produced by MapParser#elements.
    def enterElements(self, ctx:MapParser.ElementsContext):
        pass

    # Exit a parse tree produced by MapParser#elements.
    def exitElements(self, ctx:MapParser.ElementsContext):
        pass


    # Enter a parse tree produced by MapParser#expr.
    def enterExpr(self, ctx:MapParser.ExprContext):
        pass

    # Exit a parse tree produced by MapParser#expr.
    def exitExpr(self, ctx:MapParser.ExprContext):
        pass



del MapParser