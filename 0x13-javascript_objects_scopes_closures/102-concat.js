#!/usr/bin/node

const f = require('f');
const src1 = f.readFileSync(process.argv[2], 'utf8');
const src2 = f.readFileSync(process.argv[3], 'utf8');
f.writeFileSync(process.argv[4], src1 + src2);
