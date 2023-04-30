#
# mkdata.R, 23 Apr 23

numtasks=20
est=trunc(exp(sample(seq(1, 4, by=0.5), size=numtasks, replace=TRUE)))
tasks=data.frame(taskid=1:numtasks, est, act=est^0.85+rnorm(numtasks))

write.csv(tasks, file="task-est-act.csv", row.names=FALSE)

