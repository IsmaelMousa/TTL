const taskCounts = {
    backlog: 0,
    todo: 0,
    inProgress: 0,
    done: 0
};

const labels_badges = [
    "badge rounded-pill text-success text-opacity-75 fw-light bg-success bg-opacity-25 float-end",
    "badge rounded-pill text-primary text-opacity-75 fw-light bg-primary bg-opacity-25 float-end",
    "badge rounded-pill text-warning fw-light bg-warning bg-opacity-25 float-end",
    "badge rounded-pill text-danger text-opacity-75 fw-light bg-danger bg-opacity-25 float-end",
    "badge rounded-pill text-white fw-light bg-success bg-opacity-50 float-end",
    "badge rounded-pill text-white fw-light bg-danger bg-opacity-50 float-end",
    "badge rounded-pill text-white fw-light bg-primary bg-opacity-50 float-end",
    "badge rounded-pill text-white fw-light bg-warning bg-opacity-50 float-end",
];

const labelBadgeMap = {};

const priorityBadges = {
    low: "badge rounded-pill text-success text-opacity-75 fw-light bg-success bg-opacity-25",
    medium: "badge rounded-pill text-primary text-opacity-75 fw-light bg-primary bg-opacity-25",
    high: "badge rounded-pill text-warning fw-light bg-warning bg-opacity-25",
    critical: "badge rounded-pill text-danger text-opacity-75 fw-light bg-danger bg-opacity-25"
};

const currentDate = new Date();
const oneWeekLater = new Date(currentDate.getTime() + 7 * 24 * 60 * 60 * 1000);
oneWeekLater.setHours(12, 0, 0, 0);
const formattedDate = oneWeekLater.toISOString().slice(0, 16).replace("T", " ");
document.getElementById("completedAtCreate").value = formattedDate;


const alertPlaceholder = document.getElementById("taskAlert")

////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

async function fetchTaskCounts() {
    const response = await fetch("http://localhost:8000/manager/tasks/all");
    const tasks = await response.json();
    const taskCounts = {
        backlog: 0,
        todo: 0,
        inProgress: 0,
        done: 0
    };

    tasks.forEach(task => {
        const statusKey = getStatusKey(task.status);
        taskCounts[statusKey]++;
    });

    return taskCounts;
}

function getStatusKey(status) {
    switch (status) {
        case "in progress":
            return "inProgress";
        default:
            return status;
    }
}

async function updateTaskCountsFromBackend() {
    const counts = await fetchTaskCounts();
    Object.keys(counts).forEach(status => {
        taskCounts[status] = counts[status];
    });
    updateCountsDisplay();
}

const appendAlert = (message, type, iconClass) => {
    alertPlaceholder.innerHTML = "";

    const wrapper = document.createElement("div");
    wrapper.innerHTML = [
        `<div class="alert alert-${type} d-flex justify-content-between alert-dismissible" role="alert">`,
        `   <span class="${iconClass} text-${type}"> ${message["message"]}</span>`,
        '</div>'
    ].join("");

    const alertElement = wrapper.firstChild;
    alertPlaceholder.appendChild(alertElement);

    setTimeout(() => {
        alertElement.remove();
    }, 2000);
};

function updateCountsDisplay() {
    document.getElementById("backlogTasksCount").textContent = `(${taskCounts.backlog})`;
    document.getElementById("todoTasksCount").textContent = `(${taskCounts.todo})`;
    document.getElementById("inProgressTasksCount").textContent = `(${taskCounts.inProgress})`;
    document.getElementById("doneTasksCount").textContent = `(${taskCounts.done})`;
}

function getTargetContainer(taskStatus) {
    switch (taskStatus) {
        case "backlog":
            return document.getElementById("backlogTasks");
        case "todo":
            return document.getElementById("todoTasks");
        case "in progress":
            return document.getElementById("inProgressTasks");
        case "done":
            return document.getElementById("doneTasks");
        default:
            break;
    }
}

////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

document.addEventListener("DOMContentLoaded", () => {
    updateTaskCountsFromBackend();

    const tooltipTriggerList = document.querySelectorAll('[data-bs-toggle="tooltip"]')
    const tooltipList = [...tooltipTriggerList].map(tooltipTriggerEl => new bootstrap.Tooltip(tooltipTriggerEl))

    function filterTasks(searchQuery) {
        const allTasks = document.querySelectorAll(".task");
        allTasks.forEach(task => {
            const title = task.querySelector(".taskTitle").textContent.toLowerCase();
            const label = task.querySelector(".taskLabel").textContent.toLowerCase();
            const priority = task.querySelector(".taskPriority").textContent.toLowerCase();

            if (title.includes(searchQuery.toLowerCase()) ||
                label === searchQuery.toLowerCase() ||
                priority === searchQuery.toLowerCase()) {
                task.style.display = "block";
            } else {
                task.style.display = "none";
            }
        });
    }

    const searchInput = document.getElementById("searchInput");
    searchInput.addEventListener("input", () => {
        const searchQuery = searchInput.value.trim();
        filterTasks(searchQuery);
    });
    const deleteTasks = async (columnId) => {
        const tasks = document.getElementById(columnId).querySelectorAll(".task");
        tasks.forEach(task => {
            task.remove();
        });
        switch (columnId) {
            case "backlogTasks":
                await DeleteTasksByStatus("http://localhost:8000/manager/tasks/delete/status=backlog");
                taskCounts.backlog = 0;
                updateCountsDisplay();
                appendAlert({
                    "status": 200,
                    "message": "Backlog Tasks Deleted Successfully!"
                }, "danger", "bi bi-info-circle-fill");
                break;
            case "todoTasks":
                await DeleteTasksByStatus("http://localhost:8000/manager/tasks/delete/status=todo");
                taskCounts.todo = 0;
                updateCountsDisplay();
                appendAlert({
                    "status": 200,
                    "message": "To Do Tasks Deleted Successfully!"
                }, "danger", "bi bi-info-circle-fill");
                break;
            case "inProgressTasks":
                await DeleteTasksByStatus(`http://localhost:8000/manager/tasks/delete/status=${encodeURIComponent("in progress")}`);
                taskCounts.inProgress = 0;
                updateCountsDisplay();
                appendAlert({
                    "status": 200,
                    "message": "In Progress Tasks Deleted Successfully!"
                }, "danger", "bi bi-info-circle-fill");
                break;
            case "doneTasks":
                await DeleteTasksByStatus("http://localhost:8000/manager/tasks/delete/status=done");
                taskCounts.done = 0;
                updateCountsDisplay();
                appendAlert({
                    "status": 200,
                    "message": "Done Tasks Deleted Successfully!"
                }, "danger", "bi bi-info-circle-fill");
                break;
            default:
                appendAlert({
                    "status": 200,
                    "message": `${columnId.charAt(0).toUpperCase() + columnId.slice(1)} Tasks Deleted Successfully!`
                }, "danger", "bi bi-info-circle-fill");
        }
    };

    const deletionButtons = document.querySelectorAll("[id$='TasksDeletionBtn']");
    deletionButtons.forEach(button => {
        button.addEventListener("click", () => {
            const columnId = button.id.replace("DeletionBtn", "");
            deleteTasks(columnId);
        });
    });

    document.getElementById("taskCreateForm").addEventListener("submit", async function (event) {
        event.preventDefault();

        let title = document.getElementById("titleCreate").value;
        let description = document.getElementById("descriptionCreate").value;
        let label = document.getElementById("labelCreate").value;
        let status = document.getElementById("statusCreate").value;
        let priority = document.querySelector('input[name="priorityCreate"]:checked').value;
        let attachment = document.getElementById("attachmentCreate").value;
        let completed_at = document.getElementById("completedAtCreate").value;


        completed_at = completed_at.replace("T", " ")

        document.getElementById("taskCreateForm").reset();
        document.getElementById("completedAtCreate").value = formattedDate;

        const newTaskData = {
            title,
            description,
            label,
            status,
            priority,
            attachment,
            completed_at
        };

        switch (status) {
            case "backlog":
                await CreateNewTask("http://localhost:8000/manager/tasks/new", newTaskData);
                appendAlert({
                    "status": 201,
                    "message": "Backlog Task Created Successfully!"
                }, "success", "bi bi-check-circle-fill");
                break;
            case "todo":
                await CreateNewTask("http://localhost:8000/manager/tasks/new", newTaskData);
                appendAlert({
                    "status": 201,
                    "message": "To Do Task Created Successfully!"
                }, "success", "bi bi-check-circle-fill");
                break;
            case "in progress":
                await CreateNewTask("http://localhost:8000/manager/tasks/new", newTaskData);
                appendAlert({
                    "status": 201,
                    "message": "In Progress Task Created Successfully!"
                }, "success", "bi bi-check-circle-fill");
                break;
            case "done":
                await CreateNewTask("http://localhost:8000/manager/tasks/new", newTaskData);
                appendAlert({
                    "status": 201,
                    "message": "Done Task Created Successfully!"
                }, "success", "bi bi-check-circle-fill");
                break;
            default:
                break;
        }
        updateCountsDisplay();
    });
// AI Assistant -> START
    const askAIInput = document.getElementById("ai-question");
    const answerAIInput = document.getElementById("ai-answer");

    askAIInput.addEventListener("keydown", async function (event) {
        if (event.key === "Enter") {
            event.preventDefault();
            const question = askAIInput.value;
            answerAIInput.value = "";
            showLoadingIcon();
            try {
                const response = await fetch("http://localhost:8000/manager/assistants/GPT2?question=" + encodeURIComponent(question));
                const data = await response.json();
                showAIResponse(data.answer);
            } catch (error) {
                showAIResponse("An error occurred while fetching the response. Please try again later.");
            } finally {
                hideLoadingIcon();
            }
        }
    });

    function showLoadingIcon() {
        answerAIInput.value = "Loading...";
    }

    function hideLoadingIcon() {
        answerAIInput.value = "";
    }

    function showAIResponse(response) {
        let index = 0;
        const intervalId = setInterval(() => {
            if (index <= response.length) {
                answerAIInput.value = response.slice(0, index);
                index++;
            } else {
                clearInterval(intervalId);
                createResetButton();
                createCopyButton();
            }
        }, 20);
    }

    function createResetButton() {
        if (document.getElementById("askAgainButton")) {
            return;
        }

        const resetButton = document.createElement("button");
        resetButton.innerHTML = "Clear <span class='bi bi-stars'></span>";
        resetButton.id = "askAgainButton";
        resetButton.classList.add("btn", "btn-outline-danger", "btn-sm", "opacity-75", "border-0", "rounded-4", "shadow", "fw-medium", "float-end");
        resetButton.addEventListener("click", function () {
            askAIInput.value = "";
            answerAIInput.value = "";
            resetButton.remove();
            const copyButton = document.getElementById("copyAiAnswerButton");
            if (copyButton) {
                copyButton.remove();
            }
        });

        const form = document.getElementById("ai-form");
        form.appendChild(resetButton);
    }

    function createCopyButton() {
        if (document.getElementById("copyAiAnswerButton")) {
            return;
        }

        const copyButton = document.createElement("button");
        copyButton.innerHTML = "Copy <span class='bi bi-copy'></span>";
        copyButton.id = "copyAiAnswerButton";
        copyButton.classList.add("btn", "btn-outline-primary", "btn-sm", "opacity-75", "border-0", "rounded-4", "shadow", "fw-medium", "float-start");
        copyButton.addEventListener("click", function (event) {
            event.preventDefault();

            const textToCopy = answerAIInput.value;

            navigator.clipboard.writeText(textToCopy).then(function () {
                copyButton.innerHTML = "Copied! <span class='bi bi-clipboard-check-fill'></span>";
                setTimeout(() => {
                    copyButton.innerHTML = "Copy <span class='bi bi-copy'></span>";
                }, 1000);
            }, function (err) {
                console.error("Unable to copy text: ", err);
            });
        });

        const form = document.getElementById("ai-form");
        form.appendChild(copyButton);
    }


// AI Assistant -> END
});

////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
async function CreateNewTask(url, data) {
    const response = await fetch(url, {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify(data)
    });
    updateTaskCountsFromBackend();
    location.reload()
    return response.json();
}

async function UpdateTask(url, data) {
    const response = await fetch(url, {
        method: "PUT",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify(data)
    });
    updateTaskCountsFromBackend();
    location.reload()
    return response.json();
}

async function DeleteTasksByStatus(url) {
    const response = await fetch(url, {
        method: "DELETE",
        headers: {"Content-Type": "application/json"},
    });
    updateTaskCountsFromBackend();
    return response.json();
}

async function DeleteTaskById(url) {
    const response = await fetch(url, {
        method: "DELETE",
        headers: {"Content-Type": "application/json"},
    });
    updateTaskCountsFromBackend();
    return response.json();
}

////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

fetch("http://localhost:8000/manager/tasks/all", {method: "GET"})
    .then((response) => response.json())
    .then((tasks) => {
        let badgeIndex = 0;

        for (const task of tasks) {
            const priorityBadge = priorityBadges[task.priority.toLowerCase()];

            if (!labelBadgeMap[task.label]) {
                labelBadgeMap[task.label] = labels_badges[badgeIndex];
                badgeIndex = (badgeIndex + 1) % labels_badges.length;
            }

            const labelBadge = labelBadgeMap[task.label];

            const attachmentHTML = task.attachment ? `<a class="btn border border-0 taskAttachment" href="${task.attachment}" target="_blank"><span class="bi bi-paperclip text-dark opacity-50 fs-6"></span></a>` : '';


            const newTaskHTML = `
              <div id="task_${task.id}" class="task border-0 position-relative rounded-3 bg-white shadow mb-3 p-3" draggable="true">
                  <div class="float-start text-break">
                    <h6 class="h6 text-dark opacity-75 fw-light taskTitle">${task.title}</h6>
                   </div>
                   <div class="d-flex justify-content-end gap-2 mb-3">
                   <span class="${priorityBadge} taskPriority">${task.priority}</span>
                   <span class="${labelBadge} taskLabel">${task.label}</span>
                   </div>
                   
                    <p class="text-dark text-break opacity-50 fw-light taskDescription">${task.description}</p>
                    <span class="text-dark opacity-50 fw-lighter taskCompletedAt">${task.completed_at}</span>
                    ${attachmentHTML}
                    
                    
                    <button name="taskDeleteBtn" class="btn border border-0 float-end"><span class="bi bi-trash text-danger opacity-50 fs-6"></span></button>
                    <button name="taskDoneBtn" class="btn border border-0 float-end"><span class="bi bi-check2-square text-success opacity-75 fs-6"></span></button>
                    <button name="tasksEditBtn" class="btn border border-0 float-end" data-bs-toggle="modal" data-bs-target="#exampleModal"><span class="bi bi-pencil-square text-primary opacity-50 fs-6"></span></button>
                </div>
            `;
            const targetContainer = getTargetContainer(task.status);
            targetContainer.insertAdjacentHTML("beforeend", newTaskHTML);

            const latestTaskElement = targetContainer.lastElementChild;

            const deleteButton = latestTaskElement.querySelector("[name='taskDeleteBtn']");
            const taskDoneButton = latestTaskElement.querySelector("[name='taskDoneBtn']");
            const editButton = latestTaskElement.querySelector("[name='tasksEditBtn']");


            deleteButton.addEventListener("click", async function () {
                const deleteUrl = `http://localhost:8000/manager/tasks/delete/id=${task.id}`;
                await DeleteTaskById(deleteUrl);
                console.log(deleteUrl)
                this.parentNode.remove();
                appendAlert({
                    "status": 200,
                    "message": "Task Deleted Successfully!"
                }, "danger", "bi bi-info-circle-fill");
            });
            ////////////////////////////////////////////////////////////////////////////
            taskDoneButton.addEventListener("click", async function () {
                const taskElement = document.getElementById(`task_${task.id}`);
                if (taskElement.parentNode.id === "doneTasks") {
                    appendAlert({
                        "status": 200,
                        "message": "Task Already is Done!"
                    }, "warning", "bi bi-exclamation-triangle-fill");
                    return;
                }
                taskElement.remove();
                document.getElementById("doneTasks").appendChild(taskElement);

                await UpdateTask(`http://localhost:8000/manager/tasks/update/${task.id}`, {status: "done"});
                appendAlert({
                    "status": 200,
                    "message": "Task Marked as Done Successfully!"
                }, "success", "bi bi-check-circle-fill");
            });
            ////////////////////////////////////////////////////////////////////////////
            editButton.addEventListener("click", function () {
                let title = this.parentNode.querySelector(".taskTitle").textContent;
                let description = this.parentNode.querySelector(".taskDescription").textContent;
                let label = this.parentNode.querySelector(".taskLabel").textContent;
                let attachment = this.parentNode.querySelector(".taskAttachment") ? this.parentNode.querySelector(".taskAttachment").href : '';
                let completed_at = this.parentNode.querySelector(".taskCompletedAt").textContent;
                let priority = this.parentNode.querySelector(".taskPriority").textContent.toLowerCase();
                let status = "";

                switch (this.parentNode.parentNode.id) {
                    case "backlogTasks":
                        status = "backlog";
                        document.getElementById("backlogEdit").selected = true;
                        break;
                    case "todoTasks":
                        status = "todo";
                        document.getElementById("todoEdit").selected = true;
                        break;
                    case "inProgressTasks":
                        status = "in progress";
                        document.getElementById("inProgressEdit").selected = true;
                        break;
                    case "doneTasks":
                        status = "done";
                        document.getElementById("doneEdit").selected = true;
                        break;
                    default:
                        break;
                }

                completed_at = completed_at.replace("T", " ");

                document.getElementById("titleEdit").value = title;
                document.getElementById("descriptionEdit").value = description;
                document.getElementById("labelEdit").value = label;
                document.getElementById("attachmentEdit").value = attachment;
                document.getElementById("completedAtEdit").value = completed_at;
                document.getElementById(priority + "Edit").checked = true;

                const saveEditForm = document.getElementById("taskEditForm");
                saveEditForm.addEventListener("submit", async (event) => {
                    event.preventDefault();

                    const editedTask = document.getElementById(`task_${task.id}`);

                    const newTitle = document.getElementById("titleEdit").value;
                    const newDescription = document.getElementById("descriptionEdit").value;
                    const newLabel = document.getElementById("labelEdit").value;
                    const newAttachment = document.getElementById("attachmentEdit").value;
                    let newCompletedAt = document.getElementById("completedAtEdit").value;
                    const newStatus = document.getElementById("statusEdit").value;
                    const newPriority = document.querySelector('input[name="priorityEdit"]:checked').value;

                    newCompletedAt = newCompletedAt.replace("T", " ");

                    let taskAttachmentElement = editedTask.querySelector(".taskAttachment");
                    if (newAttachment && !taskAttachmentElement) {
                        taskAttachmentElement = document.createElement("a");
                        taskAttachmentElement.classList.add("btn", "border", "border-0", "taskAttachment");
                        taskAttachmentElement.href = newAttachment;
                        taskAttachmentElement.target = "_blank";
                        taskAttachmentElement.innerHTML = '<span class="bi bi-paperclip text-dark opacity-50 fs-6"></span>';
                        editedTask.appendChild(taskAttachmentElement);
                    } else if (!newAttachment && taskAttachmentElement) {
                        taskAttachmentElement.remove();
                    } else if (newAttachment && taskAttachmentElement) {
                        taskAttachmentElement.href = newAttachment;
                    }

                    const taskTitleElement = editedTask.querySelector(".taskTitle");
                    taskTitleElement.textContent = newTitle;

                    const taskDescriptionElement = editedTask.querySelector(".taskDescription");
                    taskDescriptionElement.textContent = newDescription;

                    const taskLabelElement = editedTask.querySelector(".taskLabel");
                    taskLabelElement.textContent = newLabel;

                    const taskPriorityElement = editedTask.querySelector(".taskPriority");
                    taskPriorityElement.textContent = newPriority;

                    const taskCompletedAtElement = editedTask.querySelector(".taskCompletedAt");
                    taskCompletedAtElement.textContent = newCompletedAt.replace("T", " ");

                    const editedTaskData = {
                        title: newTitle,
                        description: newDescription,
                        label: newLabel,
                        status: newStatus,
                        priority: newPriority,
                        attachment: newAttachment,
                        completed_at: newCompletedAt
                    };
                    await UpdateTask(`http://localhost:8000/manager/tasks/update/${task.id}`, editedTaskData);
                    appendAlert({
                        "status": 200,
                        "message": "Task Updated Successfully!"
                    }, "primary", "bi bi-info-circle-fill");
                });
            });

        }
    })