"""
    usage: python m_parse_test.py 
"""
import unittest

#target = __import__("fixedwidthparse.py")
#Text_csv = target.Text_csv

from fixedwidthparse import Text_csv

class TestTextCsv(unittest.TestCase):

    def test_parser(self):
        text_csv_ = Text_csv('source.txt','output.txt','spec.json',',')

        text_csv_.parse_to_csv()

        with open("output.txt",'r',encoding="windows-1252") as file:
            lines = file.read().splitlines()

            #test the header
            self.assertEqual(lines[0],'f1,f2,f3,f4,f5,f6,f7,f8,f9,f10', \
                "should be 'f1,f2,f3,f4,f5,f6,f7,f8,f9,f10'")

            #test first content line with windows-1252 characters
            self.assertEqual(lines[1],'€€€€€,bbbbbbbbbbbb,ccc,ff,ttttttttttttt,iiiiiii,gggggggggg,kkkkkkkkkkkkk,pppppppppppppppppppp,4444444444444' \
                ,"should be '€€€€€,bbbbbbbbbbbb,ccc,ff,ttttttttttttt,iiiiiii,gggggggggg,kkkkkkkkkkkkk,pppppppppppppppppppp,4444444444444'")

            #Can do more tests...

if __name__ == '__main__':
    unittest.main()
