// Generated from /home/nuvu-pc-n4gx/Personal/University/Lenguajes de programacion/Parcial 2do corte/Pt2/PythonMap.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.Lexer;
import org.antlr.v4.runtime.CharStream;
import org.antlr.v4.runtime.Token;
import org.antlr.v4.runtime.TokenStream;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.misc.*;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast", "CheckReturnValue", "this-escape"})
public class PythonMapLexer extends Lexer {
	static { RuntimeMetaData.checkVersion("4.13.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		T__0=1, T__1=2, T__2=3, T__3=4, T__4=5, T__5=6, T__6=7, T__7=8, IDENTIFIER=9, 
		STRING=10, NUMBER=11, WS=12;
	public static String[] channelNames = {
		"DEFAULT_TOKEN_CHANNEL", "HIDDEN"
	};

	public static String[] modeNames = {
		"DEFAULT_MODE"
	};

	private static String[] makeRuleNames() {
		return new String[] {
			"T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", "T__7", "IDENTIFIER", 
			"STRING", "NUMBER", "WS"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'map'", "'('", "','", "')'", "'lambda'", "':'", "'['", "']'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, null, null, null, null, null, null, null, null, "IDENTIFIER", "STRING", 
			"NUMBER", "WS"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}


	public PythonMapLexer(CharStream input) {
		super(input);
		_interp = new LexerATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@Override
	public String getGrammarFileName() { return "PythonMap.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public String[] getChannelNames() { return channelNames; }

	@Override
	public String[] getModeNames() { return modeNames; }

	@Override
	public ATN getATN() { return _ATN; }

	public static final String _serializedATN =
		"\u0004\u0000\fT\u0006\uffff\uffff\u0002\u0000\u0007\u0000\u0002\u0001"+
		"\u0007\u0001\u0002\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002\u0004"+
		"\u0007\u0004\u0002\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0002\u0007"+
		"\u0007\u0007\u0002\b\u0007\b\u0002\t\u0007\t\u0002\n\u0007\n\u0002\u000b"+
		"\u0007\u000b\u0001\u0000\u0001\u0000\u0001\u0000\u0001\u0000\u0001\u0001"+
		"\u0001\u0001\u0001\u0002\u0001\u0002\u0001\u0003\u0001\u0003\u0001\u0004"+
		"\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004"+
		"\u0001\u0005\u0001\u0005\u0001\u0006\u0001\u0006\u0001\u0007\u0001\u0007"+
		"\u0001\b\u0001\b\u0005\b3\b\b\n\b\f\b6\t\b\u0001\t\u0001\t\u0005\t:\b"+
		"\t\n\t\f\t=\t\t\u0001\t\u0001\t\u0001\n\u0004\nB\b\n\u000b\n\f\nC\u0001"+
		"\n\u0001\n\u0004\nH\b\n\u000b\n\f\nI\u0003\nL\b\n\u0001\u000b\u0004\u000b"+
		"O\b\u000b\u000b\u000b\f\u000bP\u0001\u000b\u0001\u000b\u0000\u0000\f\u0001"+
		"\u0001\u0003\u0002\u0005\u0003\u0007\u0004\t\u0005\u000b\u0006\r\u0007"+
		"\u000f\b\u0011\t\u0013\n\u0015\u000b\u0017\f\u0001\u0000\u0005\u0003\u0000"+
		"AZ__az\u0004\u000009AZ__az\u0003\u0000\n\n\r\r\"\"\u0001\u000009\u0003"+
		"\u0000\t\n\r\r  Y\u0000\u0001\u0001\u0000\u0000\u0000\u0000\u0003\u0001"+
		"\u0000\u0000\u0000\u0000\u0005\u0001\u0000\u0000\u0000\u0000\u0007\u0001"+
		"\u0000\u0000\u0000\u0000\t\u0001\u0000\u0000\u0000\u0000\u000b\u0001\u0000"+
		"\u0000\u0000\u0000\r\u0001\u0000\u0000\u0000\u0000\u000f\u0001\u0000\u0000"+
		"\u0000\u0000\u0011\u0001\u0000\u0000\u0000\u0000\u0013\u0001\u0000\u0000"+
		"\u0000\u0000\u0015\u0001\u0000\u0000\u0000\u0000\u0017\u0001\u0000\u0000"+
		"\u0000\u0001\u0019\u0001\u0000\u0000\u0000\u0003\u001d\u0001\u0000\u0000"+
		"\u0000\u0005\u001f\u0001\u0000\u0000\u0000\u0007!\u0001\u0000\u0000\u0000"+
		"\t#\u0001\u0000\u0000\u0000\u000b*\u0001\u0000\u0000\u0000\r,\u0001\u0000"+
		"\u0000\u0000\u000f.\u0001\u0000\u0000\u0000\u00110\u0001\u0000\u0000\u0000"+
		"\u00137\u0001\u0000\u0000\u0000\u0015A\u0001\u0000\u0000\u0000\u0017N"+
		"\u0001\u0000\u0000\u0000\u0019\u001a\u0005m\u0000\u0000\u001a\u001b\u0005"+
		"a\u0000\u0000\u001b\u001c\u0005p\u0000\u0000\u001c\u0002\u0001\u0000\u0000"+
		"\u0000\u001d\u001e\u0005(\u0000\u0000\u001e\u0004\u0001\u0000\u0000\u0000"+
		"\u001f \u0005,\u0000\u0000 \u0006\u0001\u0000\u0000\u0000!\"\u0005)\u0000"+
		"\u0000\"\b\u0001\u0000\u0000\u0000#$\u0005l\u0000\u0000$%\u0005a\u0000"+
		"\u0000%&\u0005m\u0000\u0000&\'\u0005b\u0000\u0000\'(\u0005d\u0000\u0000"+
		"()\u0005a\u0000\u0000)\n\u0001\u0000\u0000\u0000*+\u0005:\u0000\u0000"+
		"+\f\u0001\u0000\u0000\u0000,-\u0005[\u0000\u0000-\u000e\u0001\u0000\u0000"+
		"\u0000./\u0005]\u0000\u0000/\u0010\u0001\u0000\u0000\u000004\u0007\u0000"+
		"\u0000\u000013\u0007\u0001\u0000\u000021\u0001\u0000\u0000\u000036\u0001"+
		"\u0000\u0000\u000042\u0001\u0000\u0000\u000045\u0001\u0000\u0000\u0000"+
		"5\u0012\u0001\u0000\u0000\u000064\u0001\u0000\u0000\u00007;\u0005\"\u0000"+
		"\u00008:\b\u0002\u0000\u000098\u0001\u0000\u0000\u0000:=\u0001\u0000\u0000"+
		"\u0000;9\u0001\u0000\u0000\u0000;<\u0001\u0000\u0000\u0000<>\u0001\u0000"+
		"\u0000\u0000=;\u0001\u0000\u0000\u0000>?\u0005\"\u0000\u0000?\u0014\u0001"+
		"\u0000\u0000\u0000@B\u0007\u0003\u0000\u0000A@\u0001\u0000\u0000\u0000"+
		"BC\u0001\u0000\u0000\u0000CA\u0001\u0000\u0000\u0000CD\u0001\u0000\u0000"+
		"\u0000DK\u0001\u0000\u0000\u0000EG\u0005.\u0000\u0000FH\u0007\u0003\u0000"+
		"\u0000GF\u0001\u0000\u0000\u0000HI\u0001\u0000\u0000\u0000IG\u0001\u0000"+
		"\u0000\u0000IJ\u0001\u0000\u0000\u0000JL\u0001\u0000\u0000\u0000KE\u0001"+
		"\u0000\u0000\u0000KL\u0001\u0000\u0000\u0000L\u0016\u0001\u0000\u0000"+
		"\u0000MO\u0007\u0004\u0000\u0000NM\u0001\u0000\u0000\u0000OP\u0001\u0000"+
		"\u0000\u0000PN\u0001\u0000\u0000\u0000PQ\u0001\u0000\u0000\u0000QR\u0001"+
		"\u0000\u0000\u0000RS\u0006\u000b\u0000\u0000S\u0018\u0001\u0000\u0000"+
		"\u0000\u0007\u00004;CIKP\u0001\u0006\u0000\u0000";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}