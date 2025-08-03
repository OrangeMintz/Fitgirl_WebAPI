from fitgirl_api import FitGirlAPI

fitGirl = FitGirlAPI()

# CALL FUNCTIONS
upcoming_release = fitGirl.upcoming_release()
new_release = fitGirl.new_release()
pink_pawed = fitGirl.pink_pawed()