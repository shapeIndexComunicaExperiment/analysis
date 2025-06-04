import { cac } from 'cac';
import { DiEfficiencyMetric } from 'diefficiency';

const cli = cac('diefficiency');

cli
    .option('--exec-times <string>', 'the execution times')
    .option('-t <number>', 'the time where to evaluate the diefficiency')

cli.help();

const parsed = cli.parse();

const execTimes = parsed.options["execTimes"].split(",").map(Number);
const time = parsed.options["t"]

const granularity = 500;
const output = DiEfficiencyMetric.answerDistributionFunction(execTimes, granularity);

const diefft = DiEfficiencyMetric.defAtT(time, output.answerDist, output.linSpace);

console.log(JSON.stringify({diefft}));
