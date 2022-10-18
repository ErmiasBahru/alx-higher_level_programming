#!/usr/bin/node
/**
 * Script that computes
 * the number of tasks completed by user id
 */

const request = require('request');
const process = require('process');
const url = process.argv[2];

request.get(url, (err, _resp, body) => {
    if (err === null) {
        const data = JSON.parse(body);
        const userIds = [...new Set(data.map(todo => todo.userId))];
        const completedTasksData = {};
        userIds.forEach((id) => {
            const completedTasks = data.filter(todo => todo.userId === id && todo.completed);
            if (completedTasks.length <= 0) {
                return;
            }
            completedTasksData[id] = completedTasks.length;
        });
        console.log(completedTasksData);
    } else {
        console.log(err);
    }
});
