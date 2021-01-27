<template>
  <div class="main-component">
    <h1>TimeMan</h1>
    <hr>
    <div class="row">
      <div class="col-12">
        <h4>Create new event</h4>
        <form @submit.prevent="submitForm">
          <div class="form-group row">
            <div class="col-3">
              <input type="text" class="form form-control col-3 mx-2" placeholder="Event" v-model="table.event">
            </div>
            <div class="col-3">
              <input type="date" class="form form-control col-3 mx-2" placeholder="Start" v-model="table.start">
            </div>
            <div class="col-3">
              <input type="date" class="form form-control col-3 mx-2" placeholder="End" v-model="table.end">
            </div>
            <div class="col-3">
              <button class="btn btn-success">Submit</button>
            </div>
          </div>

        </form>
        <hr>

        <table class="table">
          <thead>
            <th>Event</th>
            <th>Start</th>
            <th>End</th>
          </thead>
          <tbody>
            <tr v-for="table in tables" :key="table.id">
              <td>{{ table.event }}</td>
              <td>{{ table.start }}</td>
              <td>{{ table.end }}</td>
              <td>
                <button class="brn btn-success btn-sm mx-1" @click="$data.table = table">Edit</button>
                <button class="brn btn-danger btn-sm mx-1" @click="deleteTable(table)">Delete</button>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </div>
</template>

<style lang="stylus" scoped>

</style>

<script>
  export default {
    name: 'Components',
    data() {
      return {
        table: {},
        tables: [],
        myDate : new Date().toISOString().slice(0,10)
      }
    },
    async created() {
      await this.getTables();
    },

    methods: {
      submitForm() {
        if (this.table.id === undefined) {
          this.createTable();
        } else {
          this.editTable();
        }
      },


      async getTables() {
        var response = await fetch('http://localhost:8000/database/tables/');
        this.tables = await response.json();
      },
      async createTable() {
        await this.getTables();

        await fetch('http://localhost:8000/database/tables/', {
          method: 'post',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify(this.table)
        });
        await this.getTables();
      },
      async editTable() {
        await this.getTables();

        await fetch(`http://localhost:8000/database/tables/${this.table.id}/`, {
          method: 'put',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify(this.table)
        });
        await this.getTables();
        this.table = {};
      },
      async deleteTable(table) {
        await this.getTables();

        await fetch(`http://localhost:8000/database/tables/${table.id}/`, {
          method: 'delete',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify(this.table)
        });
        await this.getTables();
        this.table = {};
      }
    }

  }
</script>