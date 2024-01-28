EXAMPLE1B
##HEADER##
import warnings
warnings.filterwarnings(""ignore"")
###ENDOFSEGMENT###
EXAMPLE2
##HEADER##
pd.read_csv('file', parse_dates = ['col1'], index_col = 'Year-Month')
###ENDOFSEGMENT###
