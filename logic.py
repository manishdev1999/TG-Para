import settings as settings
import common as cf


def get_options_and_analyse(questionNumber: str, paragraph):
    settingData = settings.setting[questionNumber]
    overallAnalysis = analyse_text_generate_dictonary(paragraph, settingData)
    return overallAnalysis


def analyse_text_generate_dictonary(paragraph: str, settingData):
    wordCount = cf.word_count(paragraph)
    wordCountAcceptance = cf.analyse_word_count(
        settingData["baseCount"], paragraph)
    conjuctionsCount = cf.analyse_conjunctions(
        paragraph, settingData["conjuction_list"])
    print("conjuctionsCount", conjuctionsCount)
    return {
        "wordCount": wordCount,
        "wordCountAcceptance": wordCountAcceptance
    }
