/**
 * Cria a tabela de agendamentos.
 */
function createTable() {

    return new Tabulator("#appointments-table", {

        // Dados da tabela
        data: APPOINTMENTS,

        // Ajusta automaticamente a largura das colunas
        layout: "fitColumns",

        // Mensagem exibida quando não houver registros
        placeholder: "Nenhum registro encontrado.",

        // Paginação local
        pagination: true,

        // Quantidade de registros por página
        paginationSize: 5,

        // Ordenação inicial
        initialSort: [
            {
                column: "data",
                dir: "asc"
            }
        ],

        // Colunas da tabela
        columns: [

            {
                title: "Paciente",
                field: "paciente",
                headerSort: true
            },

            {
                title: "CPF",
                field: "cpf",
                headerSort: true
            },

            {
                title: "Médico",
                field: "medico",
                headerSort: true
            },

            {
                title: "Especialidade",
                field: "especialidade",
                headerSort: true
            },

            {
                title: "Data",
                field: "data",
                headerSort: true
            },

            {
                title: "Horário",
                field: "horario",
                headerSort: true
            },

            {
                title: "Convênio",
                field: "convenio",
                headerSort: true
            },

            {
                title: "Status",
                field: "status",
                headerSort: true
            }

        ]

    });

}

/**
 * Configura o campo de pesquisa.
 */
function configureSearch(table) {

    const searchInput = document.getElementById("search-input");

    searchInput.addEventListener("keyup", function () {

        const value = this.value.trim();

        // Remove os filtros quando o campo estiver vazio
        if (value === "") {
            table.clearFilter();
            return;
        }

        // Pesquisa por paciente, CPF, médico, convênio ou status
        table.setFilter([
            [
                { field: "paciente", type: "like", value: value },
                { field: "cpf", type: "like", value: value },
                { field: "medico", type: "like", value: value },
                { field: "convenio", type: "like", value: value },
                { field: "status", type: "like", value: value }
            ]
        ]);

    });

}

// Inicializa a página
const table = createTable();
configureSearch(table);