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
    conjuctionsCountList = cf.analyse_conjunctions(
        paragraph, settingData["conjuction_list"])
    wordFrequencyInContext = cf.find_the_frequency_of_words_used(paragraph)
    paraPharseTheme = cf.predict_the_topic_of_the_paragraph(paragraph)
    return {
        "wordCount": wordCount,
        "wordCountAcceptance": wordCountAcceptance,
        "conjuctionsCountList": conjuctionsCountList,
        "wordFrequency": wordFrequencyInContext,
        "paraPharseTheme": paraPharseTheme
    }
