# Generated from Map.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .MapParser import MapParser
else:
    from MapParser import MapParser

# This class defines a complete generic visitor for a parse tree produced by MapParser.

class MapVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by MapParser#prog.
    def visitProg(self, ctx:MapParser.ProgContext):
        return self.visitChildren(ctx)



    # Visit a parse tree produced by MapParser#stat.
    def visitStat(self, ctx:MapParser.StatContext):
        
        return self.visitChildren(ctx)



    # Visit a parse tree produced by MapParser#mapFunction.
    def visitMapFunction(self, ctx:MapParser.MapFunctionContext):
        
        if ctx.lambdaExpr():
            var = ctx.lambdaExpr().ID().getText()
            functionBody = ctx.lambdaExpr().function().getText()
            iterable = ctx.iterable().getText()
            
            print(iterable)
            
            code = f"list(map(lambda {var} : {functionBody} , {iterable} ))"
            print(code)
            print(eval(code))
            
        if ctx.ID():
            ID = ctx.ID().getText()
            code  = f"list(map( {ID} , {iterable} ))"
            print(code)
            print(eval(code))
            
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MapParser#filterFunction.
    def visitFilterFunction(self, ctx:MapParser.FilterFunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MapParser#lambdaExpr.
    def visitLambdaExpr(self, ctx:MapParser.LambdaExprContext):
        
        return self.visitChildren(ctx)

    # Visit a parse tree produced by MapParser#function.
    def visitFunction(self, ctx:MapParser.FunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MapParser#op.
    def visitOp(self, ctx:MapParser.OpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MapParser#iterable.
    def visitIterable(self, ctx:MapParser.IterableContext):
        
        
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MapParser#list.
    def visitList(self, ctx:MapParser.ListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MapParser#dict.
    def visitDict(self, ctx:MapParser.DictContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MapParser#key.
    def visitKey(self, ctx:MapParser.KeyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MapParser#elements.
    def visitElements(self, ctx:MapParser.ElementsContext):
        
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MapParser#var.
    def visitVar(self, ctx:MapParser.VarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MapParser#expr.
    def visitExpr(self, ctx:MapParser.ExprContext):
        return self.visitChildren(ctx)



del MapParser