<template>
    <div>
        <table>
            <tr v-for="(line, i) in grid" :key="i">
                <td v-for="cell in line" :key="cell" :class="{celViva: cell==1}"></td>
            </tr>
        </table>
    </div>
</template>

<script>
export default {
    name: 'GameLife',
    data () {
        return {
            grid: [
                [0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0],
            ]
        }
    }
}

</script>

<style>
table, th, td {
    border: 1px solid;
}
.celViva{
    background-color: rgb(31, 245, 35);
}
.celMorta{
    background-color: rgb(124, 137, 149);
}
</style>