%% Import data
clear;clc;
T_morning = readtimetable('site001_dataprepare_forecast_morning.csv');
T_morning = movevars(T_morning, 'I', 'After', 'R_lag30');
T_morning = timetable2table(T_morning);
T_morning = removevars(T_morning, 'Datetime');

T_noon = readtimetable('site001_dataprepare_forecast_noon.csv');
T_noon = movevars(T_noon, 'I', 'After', 'R_lag30');
T_noon = timetable2table(T_noon);
T_noon = removevars(T_noon, 'Datetime');

T_evening = readtimetable('site001_dataprepare_forecast_evening.csv');
T_evening = movevars(T_evening, 'I', 'After', 'R_lag30');
T_evening = timetable2table(T_evening);
T_evening = removevars(T_evening, 'Datetime');
%% Stepwise regression using BIC criterion
mdl_morning = stepwiselm(T_morning,'quadratic','Criterion','bic')
mdl_noon = stepwiselm(T_noon,'quadratic','Criterion','bic')
mdl_evening = stepwiselm(T_evening,'quadratic','Criterion','bic')
save stepwise-result
%% Load model
clc;clear;load stepwise-result.mat
% Show list of selected features
morning_list = append('[',strjoin(strcat('''',mdl_morning.CoefficientNames, ''''), ', '),']')

noon_list = append('[',strjoin(strcat('''',mdl_noon.CoefficientNames, ''''), ', '),']')

evening_list = append('[',strjoin(strcat('''',mdl_evening.CoefficientNames, ''''), ', '),']')
