insert into programs values (1, 'математика и информационные технологии');
insert into programs values (2, 'теоретическая физика');

insert into courses values (1, 'Алгебра');
insert into courses values (2, 'Дискретная математика');
insert into courses values (3, 'Математический анализ');
insert into courses values (4, 'Физика');
insert into courses values (5, 'Физическая культура');

insert into programs_courses values (1, 1, 2);
insert into programs_courses values (1, 2, 1);
insert into programs_courses values (1, 3, 1);
insert into programs_courses values (1, 3, 2);
insert into programs_courses values (1, 4, 1);
insert into programs_courses values (1, 4, 2);
insert into programs_courses values (1, 5, 1);
insert into programs_courses values (1, 5, 2);

insert into marks values (1, 2, 3);
insert into marks values (1, 3, 5);
insert into marks values (1, 4, 3);
insert into marks values (1, 5, 4);
insert into marks values (2, 1, 2);
insert into marks values (2, 4, 5);
insert into marks values (2, 5, 4);
insert into marks values (3, 1, 3);
insert into marks values (3, 3, 5);
insert into marks values (3, 4, 4);
insert into marks values (3, 5, 5);

insert into students(program_id, card, surname, name) values(1, '180101', 'Нагай', 'Илья');
insert into students(program_id, card, surname, name) values(2, '180201', 'Скворцов', 'Данила');
insert into students(program_id, card, surname, name) values(2, '180301', 'Сорокина', 'Екатерина');
